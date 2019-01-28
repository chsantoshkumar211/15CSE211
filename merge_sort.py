import random
import time
def merge_sort(a): 
    if len(a) >1: 
        m = len(a)//2
        L = a[:m]
        R = a[m:] 

        merge_sort(L) 
        merge_sort(R)
        i=0
        j=0
        k=0
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                a[k] = L[i] 
                i+=1
            else: 
                a[k] = R[j] 
                j+=1
            k+=1
        
        while i < len(L): 
            a[k] = L[i] 
            i+=1
            k+=1
        
        while j < len(R): 
            a[k] = R[j] 
            j+=1
            k+=1
f=open("merge-out.txt",'w')
a=[]
a1=[]
a2=[]
for i in range(0,99):
    a.append(random.randint(1,100))
for i in range(0,999):
    a1.append(random.randint(1,100))
for i in range(0,99999):
    a2.append(random.randint(1,100))

t1=time.time()
merge_sort(a)
t2=time.time()
f.write("Time taken for merge sort with 100 elements in seconds: "+str(t2-t1))

t1=time.time()
merge_sort(a1)
t2=time.time()
f.write("\nTime taken for merge sort with 10000 elements in seconds: "+str(t2-t1))

t1=time.time()
merge_sort(a2)
t2=time.time()
f.write("\nTime taken for merge sort with 100000 elements in seconds: "+str(t2-t1))

f.close()