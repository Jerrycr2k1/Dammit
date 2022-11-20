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
    return data.split("-")

def getData(data):
    dongs = tachDong(data)
    for i in dongs:
        dauVsCuoi = tachDinh(i)
        dinh = tachTrongSo(dauVsCuoi[0])
        gTrongSoDinh.update({dinh[0].strip() : dinh[1] if len(dinh) > 1 else 0})
        dinhCuoi = []
        for j in tachNut(dauVsCuoi[1]):
            dinhCuoi.append(tachTrongSo(j.strip())[0])
        # Sắp xếp
        dinhCuoi.sort()
        gNext.update({dinh[0].strip() : dinhCuoi})
        
def ss(node):
    return int(gTrongSoDinh[node])
def s(node):
    return node

def bfs(visited, gNext, start, end, l, mapp, isBFS):
    visited.add(start)
    if start == end:
        result.write( start + " | Dừng".ljust(28)+ "|\n")
        return
    if len(l) == 0 and len(gNext[start]):
        result.write( start + " | Dừng".ljust(28)+ "|\n")
        result.write( "Không tìm thấy!")
        return 
    for i in gNext[start]:
        if i not in visited:
            visited.add(i)
            l.append(i)
            mapp.update({i : start})
    if isBFS:
        l.sort(key=ss)
    if len(l) == 0:
        result.write( start + " | Dừng".ljust(28)+ "|\n")
        result.write( "Không tìm thấy!")
        return 
    nextp = l[0]
    result.write(vebang(start, gNext[start] , l, isBFS) + "\n")
    l.pop(0)
    bfs(visited, gNext, nextp, end, l, mapp, isBFS)

def vebang(start, listKe, l, isBFS):
    if isBFS:
        danhSachKe = [ i + "("+gTrongSoDinh[i].strip()+")" for i in listKe]
        danhSachL = [ i + "("+gTrongSoDinh[i].strip()+")" for i in l]
        
        string = start + " | " + ", ".join(danhSachKe).ljust(24) + " | " + ", ".join(danhSachL)
        return string
    return start + " | " + ", ".join(listKe).ljust(24) + " | " + ", ".join(l)

gNext = {}
gTrongSoDinh = {}

getData(data)
fobj.close()
visited = set()
mapp = {}
l = []
end = 'A'
start = 'A'

start = input("Điểm bắt đầu: ").upper().strip()
end = input("Điểm Kết thúc: ").upper().strip()
isBFS = int(input("Thuật toán Tốt nhất đầu tiên:\nYes: 1 | No: 0\n"))
duongDi = []
result.write("TT|       Danh sách kề       | Danh sách L\n" )
bfs(visited, gNext, start, end, l, mapp, isBFS)
while(end != start):
    duongDi.append(end)
    end = mapp[end]
duongDi.append(end)
duongDi.reverse()
# print(" -> ".join(duongDi))
result.write("Đường đi: \n" + " -> ".join(duongDi))
result.close()
result = open('result.txt', 'r', encoding = 'utf-8')
print(result.read())
