class Vertex:
    def __init__(self, id):
        self.id = id
        self.neighbours = set()
        self.weights = {}
    
    def addNeigh(self, neigh, weight):
        self.neighbours.add(neigh)
        self.weights[neigh] = weight

    def __str__(self):
        s = f'{self.id}'
        for neigh in self.neighbours:
            s+= f'\t{neigh}: {self.weights[neigh]}'
        return s

def dijkstra(graph, s):

    dist = {k:float('inf') for k in graph.keys()}
    queue = set([k for k in graph.keys()])

    dist[s] = 0
    
    while len(queue) > 0:
        # get node with min dist
        mindist = float('inf')
        u = next(iter(queue))
        for v in queue:
            if dist[v] < mindist:
                mindist = dist[v]
                u = v
        queue.remove(u)
        # print(queue)

        for neigh in graph[u].neighbours: 
            if neigh not in queue:
                continue
            newdist = dist[u] + graph[u].weights[neigh]
            if newdist < dist[neigh]:
                dist[neigh] = newdist
    return dist

import random

# graph creation
graph = {}
total_vertices = 10
for i in range(total_vertices):
    v = Vertex(i)
    graph[i] = v
    for j in range(total_vertices):
        if i == j:
            continue
        v.addNeigh(j, random.randint(1, 9))

    print(v)
    
starting_point = 0
dist = dijkstra(graph, starting_point)
print(dist)
