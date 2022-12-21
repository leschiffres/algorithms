edges = [[1,2],[2,3],[3,4],[4,5],[1,5]]
# edges = [[1,2],[2,3],[3,4],[4,5]]
edges = [[1,2],[1,3],[2,4]]
edges = [[4,7],[4,8],[5,6],[1,6],[3,7],[2,5],[5,8],[1,2],[4,9],[6,10],[8,10],[3,6],[2,10],[9,10],[3,9],[2,3],[1,9],[4,6],[5,7],[3,8],[1,8],[1,7],[2,4]]

graph = {}
for u,v in edges:
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    
    graph[u].append(v)
    graph[v].append(u)

visited = {k:False for k in graph.keys()}

# Iterate over all nodes and their neighbours
# if a neighbour is already visited then there is a cycle
# if no cycle has been found at the end then there is no cycle

def dfs(node, parent):
    print(f"visiting node {node}")
    visited[node] = True
    for v in graph[node]:
        if v == parent: continue
        if visited[v]:
            print(f"Node {v} is already visited")
            return True
        else:
            if dfs(v, node):
                return True
    return False

def cycle_test(graph):
    nodes = list(graph.keys())
    for k in nodes:
        if visited[k]:
            continue
        has_cycle = dfs(k, k)
        if has_cycle:
            print
            return True
    return False

if cycle_test(graph):
    print("Graph has a cycle")
else:
    print("Graph does not have a cycle")