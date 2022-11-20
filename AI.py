graph = {}
fobj = open('graph.txt')
data = fobj.read()

for i in data.split("\n"):
    try:
        key = i.split(":")[0].strip()
        value = i.split(":")[1].strip()
        value = [j.strip() for j in value.split(",")] if len(value) > 0 else []
        value.sort()
        graph.update({key : value})
    except:
        continue

visited = set()
mapping = []

def dfs(visited, graph, start, end):  
    graph[start].reverse()
    if start == end:
        mapping.append(start)
        return True
    for i in graph[start]:
        if i not in visited:
            visited.add(start)
            if(dfs(visited, graph, i, end)):
                mapping.append(start)
                return True

print("Following is the Depth-First Search")
dfs(visited, graph, 'A', 'H')
mapping.reverse()
print(" -> ".join(mapping))
