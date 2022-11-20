graph = {}
fobj = open('data3.txt')
result = open('result.txt', 'w', encoding = 'utf-8')
data = fobj.read()

def tachDong(data):
    return data.split("\n")
def tachDinh(data):
    return data.split(":")
def tachNut(data):
    return data.split(",")
def tachTrongSo(data):
    if "-" not in data:
        data = data + " -0"
    return data.split("-")


def getData(data):
    dongs = tachDong(data)
    for i in dongs:
        dauVsCuoi = tachDinh(i)
        dinh = tachTrongSo(dauVsCuoi[0])
        gTrongSoDinh.update({dinh[0].strip() : dinh[1] if len(dinh) > 1 else 0})
        dinhCuoi = []
        for j in tachNut(dauVsCuoi[1]):
            k.update({dinh[0] + tachTrongSo(j)[0] : int(tachTrongSo(j)[1])})
            dinhCuoi.append(tachTrongSo(j.strip())[0])
        # Sắp xếp
        dinhCuoi.sort()
        gNext.update({dinh[0].strip() : dinhCuoi})
        
def PrintDic(data):
    for i in data:
        print(i, ':' , data[i])
def s(node):
    return node
def soF(node):
    return int(f[node])

def bfs(visited, gNext, start, end, l, mapp):
    visited.add(start)
    if start == end:
        result.write( start + " | Dừng".ljust(25)+ "|\n")
        return True
    strings = []
    for i in gNext[start]:
        if i == ' ':
            continue
        g[i] = g[start] + k[start + ' ' + i]
        fi = g[i] + int(gTrongSoDinh[i])
        string = start + " | " + i + " | " + str(k[start + ' ' + i]).ljust(3) + "| " + gTrongSoDinh[i].ljust(3) + "| " + str(g[i]).ljust(3) + "| " + str(fi) + " |"
        strings.append(string)
        # print(string)
        # print("l", l)
        # print("F", f)
        if f[i] > fi or i not in l:
            f.update({i :fi})
            mapp.update({i : start})
        if i not in l: 
            l.append(i)

    l.sort()            
    l.sort(key=soF)

    result.write("\n".join(strings))
    result.write(" " + ", ".join([ i + "("+str(f[i])+")" for i in l]).ljust(20) + "\n")
    result.write("-".join(["-" for gach in range(30)]) + "\n")
    if len(l) == 0:
        return False;
    nextp = l[0]
    l.pop(0)
    visited.add(nextp)
    return bfs(visited, gNext, nextp, end, l, mapp)

gNext = {}
gTrongSoDinh = {}
k = {}
f = {}

getData(data)
fobj.close()
visited = set()
mapp = {}
l = []
end = 'B'
start = 'A'
g = {}
for i in gTrongSoDinh:
    g.update({i : 0})
    f.update({i : 0})

start = input("Điểm bắt đầu: ").upper()
end = input("Điểm Kết thúc: ").upper()
duongDi = []
result.write("TT|      Danh sách kề     | Danh sách L\n" )
check = bfs(visited, gNext, start, end, l, mapp)
if check:
    while end != start:
        duongDi.append(end)
        end = mapp[end]
    duongDi.append(end)
    duongDi.reverse()
    result.write("Đường đi: \n" + " -> ".join(duongDi))
    result.close()
    result = open('result.txt', 'r', encoding = 'utf-8')
    print(result.read())
else:
    result.close()
    result = open('result.txt', 'w', encoding = 'utf-8')
    print("Không tìm thấy đường!")
    result.write("Không tìm thấy đường!")
    result.close()
