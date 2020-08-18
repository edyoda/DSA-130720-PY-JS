graph = {}

function addEdge(u,v)
    {if(u in graph)
        {
        graph[u].push(v)
        }
    else{
        graph[u] = [v]}
    }
function printEdges()
    {
        for (each_vertex in graph)
        {
            for(its_adjacent in graph[each_vertex])
            {
            console.log(each_vertex,"------",graph[each_vertex][its_adjacent])
            }
        }
    }

addEdge("A","B")
addEdge("A","C")
addEdge("A","D")
addEdge("B","A")
addEdge("C","A")
addEdge("C","D")
addEdge("D","A")
addEdge("D","C")

console.log(graph)

printEdges()