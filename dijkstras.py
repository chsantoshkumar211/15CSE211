from collections import defaultdict 
import sys 

class Heap(): 

    def __init__(self): 
        self.array = [] 
        self.size = 0
        self.pos = [] 

    def newMinHeapNode(self, v, dist): 
        minHeapNode = [v, dist] 
        return minHeapNode 
    def swapMinHeapNode(self,a, b): 
        t = self.array[a] 
        self.array[a] = self.array[b] 
        self.array[b] = t 

    def minHeapify(self, idx): 
        smallest = idx 
        left = 2*idx + 1
        right = 2*idx + 2

        if left < self.size and self.array[left][1] < self.array[smallest][1]: 
            smallest = left 

        if right < self.size and self.array[right][1] < self.array[smallest][1]: 
            smallest = right
        if smallest != idx:
            self.pos[ self.array[smallest][0] ] = idx 
            self.pos[ self.array[idx][0] ] = smallest  
            self.swapMinHeapNode(smallest, idx) 
            self.minHeapify(smallest)
    def extractMin(self):
        if self.isEmpty() == True:
            return
        root = self.array[0] 
        lastNode = self.array[self.size - 1] 
        self.array[0] = lastNode 
        self.pos[lastNode[0]] = 0
        self.pos[root[0]] = self.size - 1
        self.size -= 1
        self.minHeapify(0) 
        return root 

    def isEmpty(self): 
        return True if self.size == 0 else False

    def decreaseKey(self, v, dist): 
        i = self.pos[v]
        self.array[i][1] = dist 
        while i > 0 and self.array[i][1] < self.array[(i - 1) / 2][1]: 

            self.pos[ self.array[i][0] ] = (i-1)/2
            self.pos[ self.array[(i-1)/2][0] ] = i 
            self.swapMinHeapNode(i, (i - 1)/2 ) 
            i = (i - 1) / 2; 
    def isInMinHeap(self, v): 
        if self.pos[v] < self.size: 
            return True
        return False
def printArr(dist, n): 
    sr=65
    for i in range(n): 
        out.write("Shortest path from A to "+chr(sr)+" is "+str(dist[i])+"\n") 
        sr+=1


class Graph(): 

	def __init__(self, V): 
		self.V = V 
		self.graph = defaultdict(list)
	def addEdge(self, src, dest, weight):
		newNode = [dest, weight] 
		self.graph[src].insert(0, newNode)
		newNode = [src, weight] 
		self.graph[dest].insert(0, newNode)
	def dijkstra(self, src): 

		V = self.V 
		dist = []
		minHeap = Heap()
		for v in range(V): 
			dist.append(sys.maxint) 
			minHeap.array.append( minHeap.newMinHeapNode(v, dist[v]) ) 
			minHeap.pos.append(v)
		minHeap.pos[src] = src 
		dist[src] = 0
		minHeap.decreaseKey(src, dist[src]) 
		minHeap.size = V;  
		while minHeap.isEmpty() == False: 
			newHeapNode = minHeap.extractMin() 
			u = newHeapNode[0]
			for pCrawl in self.graph[u]: 

				v = pCrawl[0] 
				if minHeap.isInMinHeap(v) and dist[u] != sys.maxint and	pCrawl[1] + dist[u] < dist[v]: 
						dist[v] = pCrawl[1] + dist[u]
						minHeap.decreaseKey(v, dist[v]) 

		printArr(dist,V) 
out=open("out.txt","a")
out.write("Shortest paths from vertex A of graph 2:\n")
with open("graph.txt","r") as f:
    i=0
    for line in f:
        i+=1
        if(i==7):
            break
    graph = Graph(7)
    i=0
    for line in f:
        l=str(line).split()
        v=1
        w=2
        while(w<len(l)):
            graph.addEdge(i,int(l[v])-1,int(l[w]))
            w=w+2
            v=v+2
        i+=1
        if(i==7):
            break
    graph.dijkstra(0)
    f.close()
    