class Graph:
    def __init__(self, n):
        self.n=n
        self.adj=[[]*n for i in range(n)]
        print(self.adj)
    def edge(self,x,y):
        self.adj[x-1].append(y-1)
        self.adj[y-1].append(x-1)
        print(self.adj)
    def BFS(self, source):
        visited=[False]*self.n
        distance=[-1]*self.n
        res=[]
        queue=[]
        queue.append(source)
        visited[source]=True
        distance[source]=0
        while len(queue) > 0:
            s=queue.pop(0)
            res.append(s)
            for item in self.adj[s]:
                if visited[item]==False:
                    queue.append(item)
                    visited[item]=True
                    distance[item]=distance[s]+1
        return distance

graph1=Graph(4)
graph1.edge(1,4)
graph1.edge(4,3)
graph1.edge(3,2)
graph1.edge(2,1)
#graph1.edge(4,3)
distance=graph1.BFS(0)
print("The distance of each node from Node O is:", distance)

