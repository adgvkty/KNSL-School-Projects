from collections import defaultdict
import random as ra
 
class Graph:

    result = ''
    
    def __init__(self):
        self.graph = defaultdict(list)
 
    def add_edge(self, u, v):
        self.graph[u].append(v)
 
    def dfs_r(self, v, visited):
        visited.add(v)
        
        #print(v, end=' -> ')

        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.dfs_r(neighbour, visited)
    
    def DFS(self, v):
        global results, apexes
        
        visited = set()
        self.dfs_r(v, visited)
        if len(visited) < len(apexes):
            result = 'No'
        else:
            result = 'Yes'
        return result
            
results = [0, 0]

g = Graph()
apexes = []

def main():
    global apexes, results
    
    for i in range(100):
        apexes = []
        apexes = [i for i in range(1, ra.randint(5, 10))]
        
        for i in range(len(apexes)):
            g.add_edge(i, ra.randint(1, len(apexes)))
        g.DFS(ra.randint(1, len(apexes)))
    return results

#print(main())