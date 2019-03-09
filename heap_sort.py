import time
import random
def heapify(a, n, i): 
    maxx = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and a[i] < a[l]: 
        maxx = l 

    if r < n and a[maxx] < a[r]: 
        maxx = r 

    if maxx != i: 
        a[i],a[maxx] = a[maxx],a[i]

        heapify(a, n, maxx) 

def heapSort(a): 
    n = len(a) 
    for i in range(n, -1, -1): 
        heapify(a, n, i)  
    for i in range(n-1, 0, -1): 
        a[i], a[0] = a[0], a[i]
        heapify(a, i, 0) 

f=open("heap-out.txt","w")
a=[]
a1=[]
a2=[]
for i in range(0,1000):
    a.append(random.randint(0,100))
for i in range(0,10000):
    a1.append(random.randint(0,100))
for i in range(0,100000):
    a2.append(random.randint(0,100))

t1=time.time()
heapSort(a)
t2=time.time()
f.write("\nTime taken for heap sort with 1000 elements in seconds: "+str(t2-t1))

t1=time.time()
heapSort(a1)
t2=time.time()
f.write("\nTime taken for heap sort with 10000 elements in seconds: "+str(t2-t1))

t1=time.time()
heapSort(a2)
t2=time.time()
f.write("\nTime taken for heap sort with 100000 elements in seconds: "+str(t2-t1))


