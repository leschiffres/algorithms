n = 6
edges = [[0,1],[0,2],[3,5],[5,4],[4,3], [2,4]]
source = 0
destination = 5

graph = {i:[] for i in range(n)}
for u,v in edges:
    graph[u].append(v)
    graph[v].append(u)

visited = {k:False for k in graph.keys()}
paths = {k:"" for k in graph.keys()}

def dfs(node, path):
    visited[node] = True
    path += str(node) + '-'
    paths[node] = path
    for v in graph[node]:
        if visited[v] == False:
            dfs(v, path)

dfs(source, "")

print(paths)

path_exists = visited[destination]

if path_exists:
    print(f"Path between node {source} and {destination}: {paths[destination]}")
else:
    print(f"Path does NOT exist between node {source} and {destination}")