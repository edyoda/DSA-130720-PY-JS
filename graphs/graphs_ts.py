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

    def Explore(self,v,visited,stack):
        visited[v] = True
        # print(v,"->Explored ")
        for w in self.graph[v]:
            if visited[w] == False:
                self.Explore(w,visited,stack)
        stack.append(v)
    #Narpath: this explore will call itself untill it reach its last neighbour and 
    # as the final call was Explore(v) we append v


    def TS(self):
        visited = [False] * (max(self.graph.keys())+1)
        stack = []
        # print(len(visited),visited)
        for v in self.graph.keys():
            if visited[v] == False:
                # print("in dfs",v)
                self.Explore(v,visited,stack)
        print(stack[::-1]) # print stack in revrse order

g = graph()


# g.addEdge(0, 1)
# g.addEdge(1, 2) 
# g.addEdge(2, 3)
# g.addEdge(2, 4)
# g.addEdge(2, 5)
# g.addEdge(7, 6)
# g.addEdge(6, 5)

g.addEdge(0, 2)
g.addEdge(1, 2) 
g.addEdge(1, 3)
g.addEdge(2, 4)
g.addEdge(4, 7)
g.addEdge(3, 5)
g.addEdge(4, 5)
g.addEdge(5, 6)



print("*******************************************")
# print(g.graph)
g.TS()