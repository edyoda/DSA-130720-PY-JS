class graph:
    def __init__(self):
        self.graph = {}

    def addEdge(self,u,v):
        if u in self.graph.keys():
            self.graph[u].append(v)
        else:
            self.graph[u] = [v]
        if v not in self.graph:
            self.graph[v]=[]

    def Explore(self,v,visited):
        visited[v] = True
        print(v,"->Explored ")
        for w in self.graph[v]:
            if visited[w] == False:
                self.Explore(w,visited)

    def DFS(self):
        visited = [False] * (max(self.graph.keys())+1)
        print(len(visited),visited)
        for v in self.graph.keys():
            if visited[v] == False:
                print("in dfs",v)
                self.Explore(v,visited)

g = graph()
# g.addEdge(0,1)
# g.addEdge(0,2)
# g.addEdge(0,3)
# g.addEdge(2,3)

# g.addEdge(1,0)
# g.addEdge(2,0)
# g.addEdge(3,0)
# g.addEdge(3,2)

# g.addEdge(0, 1) 
# g.addEdge(0, 2) 
# g.addEdge(1, 2) 
# g.addEdge(2, 0) 
# g.addEdge(2, 3) 
# print(g.graph)

# g.addEdge(0, 1) 
# g.addEdge(0, 2) 
# g.addEdge(1, 2) 
# g.addEdge(2, 0) 
# g.addEdge(2, 3) 
# g.addEdge(3, 3)


g.addEdge(5, 2) 
g.addEdge(5, 0) 
# g.addEdge(4, 0) 
# g.addEdge(4, 1) 
g.addEdge(2, 3) 
g.addEdge(3, 1)
print("*******************************************")
print(g.graph)
g.DFS()


