# https://leetcode.com/problems/number-of-provinces/
# https://leetcode.com/problems/number-of-operations-to-make-network-connected/
        
# given a set of edges and a number n denoting the total number of nodes in the graph
# with ids from 0 to n-1, compute the number of connected components in the graph

edges = [[0,1],[0,2],[0,3],[1,2],[1,3]]
n = 6
# transform the edges into a graph dictionary where each key denotes a node id and 
# the dictionary in the key k contains all the neighbours of node k
graph = {i:[] for i in range(n)}
for u,v in edges:
	graph[u].append(v)
	graph[v].append(u)
# print(graph)        
        
# run dfs to find all the connected components
visited = {k:False for k in graph.keys()}
        
def dfs(temp, node):
	visited[node] = True
	temp.append(node)
	            
	for v in graph[node]:
		if visited[v] == False:
			temp = dfs(temp, v)
	return temp
        
# connected components
cc = []
for k in graph.keys():
	if visited[k] == False:
		temp = []
		cc.append(dfs(temp, k))
        
print(cc)
