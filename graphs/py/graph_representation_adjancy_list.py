graph = {}

def addEdge(u,v):
    if u in graph.keys():
        graph[u].append(v)
    else:
        graph[u] = [v]

def printEdges():
    for each_vertex in graph:
        for its_adjacent in graph[each_vertex]:
            print(each_vertex,"------",its_adjacent)

addEdge("A","B")
addEdge("A","C")
addEdge("A","D")
addEdge("B","A")
addEdge("C","A")
addEdge("C","D")
addEdge("D","A")
addEdge("D","C")

print(graph)

printEdges()




