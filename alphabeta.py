import math
input = {
'A' : ['B', 'C', 'D'],
'B' : ['E', 'F'],
'C' : [7, 8, 'G'],
'D' : ['H', 'I', 'J'],
'E' : [2, 6],
'F' : [5, 6, 3],
'G' : [9, 1, 3],
'H' : [5, 2, 4],
'I' : [7],
'J' : [9, 4],
}

def PrintTab(tab):
    for i in range(tab):
        print("\t", end = "")
def PrintNode(node, tab, val, cut = False):
    PrintTab(tab)
    if type(node) == type(val):
        val = ""    
    if cut:
        print(node, val, " Cắt")
    else:
        print(node, val)
def minimax(node, alpha, beta, IsMax, tab = 0):
    if type(node) == type(1):  
        return node
    cut = False
    if IsMax:
        val= -math.inf
        for child in input[node] :
            if cut:
                PrintNode(child, tab + 1, val, True)
                continue

            eva = minimax(child, alpha, beta, False, tab + 1)
            val = max(val, eva)
            alpha= max(alpha, val)

            if beta<=alpha:
                cut = True

            PrintNode(child, tab + 1, eva)
    else:
        val= +math.inf
        for child in input[node]:
            if cut:
                PrintNode(child, tab + 1, val, True)
                continue

            eva = minimax(child, alpha, beta, True, tab + 1)
            val = min(val, eva)
            beta = min(beta, eva)

            if beta<=alpha:
                cut = True

            PrintNode(child, tab + 1, eva)

    if tab == 0:
        print(node, val)
    return val 

print(minimax('A', -math.inf, math.inf, True))

