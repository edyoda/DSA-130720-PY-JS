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

    def BFS(self):
        visited = [False] * (max(self.graph.keys())+1)
        queue = []
        for v in self.graph.keys():
            if visited[v]==True:
                continue
            queue.append(v)
            visited[v] = True
            while len(queue)!=0:
                s = queue.pop(0) # removes from the front
                print(s,end="-->")
                for i in self.graph[s]:
                    if visited[i] == False:
                        queue.append(i)
                        visited[i] = True

g = graph()
g.addEdge(0, 2)
g.addEdge(1, 2) 
g.addEdge(1, 3)
g.addEdge(2, 4)
g.addEdge(4, 7)
g.addEdge(3, 5)
g.addEdge(4, 5)
g.addEdge(5, 6)

g.BFS()