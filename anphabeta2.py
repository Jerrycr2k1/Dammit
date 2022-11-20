import math
graph = {}
fobj = open('inputab.txt')
data = fobj.read()
begin = ""

def tachDong(data):
    return data.split("\n")
def tachDinh(data):
    return data.split(":")
def tachNut(data):
    return data.split(",")

input = {}
def getData(data):
    dongs = tachDong(data)
    for i in dongs:
        nodeAndChild = tachDinh(i)
        node = nodeAndChild[0].strip()
        child = []
        for j in tachNut(nodeAndChild[1]):
            j = j.strip()
            try:
                j = int(j)
            except:
                j = str(j)
            finally:
                child.append(j)
        input.update({node : child})

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

getData(data)
for i in input:
    begin = i
    break
minimax(begin, -math.inf, math.inf, True, 0)
