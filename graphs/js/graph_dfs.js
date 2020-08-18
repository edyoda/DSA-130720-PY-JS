function getMax(obj) {
    return Math.max.apply(null,Object.keys(obj));
  }

class Graph{
    constructor()
        {
        this.graph = {}
        }
    addEdge(u,v){
        {if(u in this.graph)
            {
            this.graph[u].push(v)
            }
        else{
            this.graph[u] = [v]}
        }
        if(!(v in this.graph)){
            this.graph[v] = []
        }
    }
    Explore(v,visited)
        {
        visited[v] = true
        console.log(v,"->Explored ")
            for(var w of this.graph[v])
            {
                if(visited[w]==false){
                    this.Explore(w,visited)
                }
            }
        }

    DFS(){
        const visited = new Array()
        const visited_length = getMax(this.graph)+1
        for(var i=0;i<visited_length;i++){
            visited.push(false)
        }
        for(var v in this.graph){
            if(visited[v] == false)
            {
                console.log("in dfs",v)
                this.Explore(v,visited)
            }
        }
    }
}
g = new Graph();


// g.addEdge(0,1)
// g.addEdge(0,2)
// g.addEdge(1,3)
// g.addEdge(3,6)
// g.addEdge(1,5)
// g.addEdge(5,7)
// g.addEdge(4,8)
// g.addEdge(4,9)
// g.addEdge(2,4)
// console.log("*******************************************")
// console.log(g.graph)
// g.DFS()