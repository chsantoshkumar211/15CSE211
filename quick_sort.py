import random
import time

def median(arr,l,r):
    mid=(l+r)//2
    if(arr[l]>arr[r]):
        t=arr[l]
        arr[l]=arr[r]
        arr[r]=t
    if(arr[l]>arr[mid]):
        t=arr[l]
        arr[l]=arr[mid]
        arr[mid]=t
    if(arr[mid]>arr[r]):
        t=arr[mid]
        arr[mid]=arr[r]
        arr[r]=t
    t=arr[mid]
    arr[mid]=arr[r-1]
    arr[r-1]=t
    return arr[r-1]

def partition(arr,l,h): 
    i = ( l-1 ) 
    pivot = median(arr,l,h) 
  
    for j in range(l , h): 
        if   arr[j] <= pivot: 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[h] = arr[h],arr[i+1] 
    return ( i+1 ) 

def quick_sort(arr,l,h): 
    if len(arr)>30:
        if l < h: 
            pi = partition(arr,l,h) 
            quick_sort(arr, l, pi-1) 
            quick_sort(arr, pi+1, h) 
    else:
        selection(arr)
def selection(a):
    for i in range(0,len(a)):
        m = i
        for j in range(i,len(a)):
            if a[j]<a[m]:
                m=j
        temp=a[i]
        a[i]=a[m]
        a[m]=temp
f=open("quick-out.txt","w")
a=[]
a1=[]
a2=[]
for i in range(0,99):
    a.append(random.randint(1,100))
for i in range(0,9999):
    a.append(random.randint(1,100))
for i in range(0,49999):
    a.append(random.randint(1,100))

t1=time.time()
quick_sort(a,0,len(a)-1) 
t2=time.time()
f.write("Time taken for quick sort with 100 elements in seconds: "+str(t2-t1))

t1=time.time()
quick_sort(a1,0,len(a1)-1) 
t2=time.time()
f.write("\nTime taken for quick sort with 10000 elements in seconds: "+str(t2-t1))

t1=time.time()
quick_sort(a2,0,len(a2)-1) 
t2=time.time()
f.write("\nTime taken for quick sort with 50000 elements in seconds: "+str(t2-t1))
