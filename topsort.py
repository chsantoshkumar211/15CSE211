from collections import defaultdict 

class Graph: 
    def __init__(self,vertices): 
        self.graph = defaultdict(list)
        self.V = vertices 

    def addEdge(self,u,v): 
        self.graph[u].append(v) 

    def topologicalSortUtil(self,v,visited,stack): 
        visited[v] = True
        for i in self.graph[v]: 
            if visited[i] == False: 
                self.topologicalSortUtil(i,visited,stack)
        stack.insert(0,v)
    def topologicalSort(self):
        visited = [False]*self.V 
        stack =[]
        for i in range(self.V): 
            if visited[i] == False: 
                self.topologicalSortUtil(i,visited,stack)
        out.write("The topological sort of the first graph is: \n")
        sr=65
        for i in range(len(stack)-1,-1,-1):
            out.write(chr(sr)+" "+str(stack[i]+1)+"\n")
            sr+=1
        out.write("\n")
g=Graph(7)
i=0
out=open("out.txt","w")
with open("graph.txt","r") as f:
    for line in f:
        l=str(line).split()
        v=1
        while v<len(l):
            g.addEdge(int(l[v])-1,i)
            v+=2
        i+=1
        if i>=7:
            break
g.topologicalSort()
f.close()
