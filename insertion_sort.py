import time
import random

f = open("insertion-out.txt", "w")

a=[None]*100000

for i in range(0,100):
    a[i]=random.randint(1,100)

t1=time.time()
for i in range(1,100):
    key = a[i]
    j=i-1
    while j>=0 and key<a[j]:
        a[j+1]=a[j]
        j-=1
    a[j+1]=key
t2=time.time()
f.write("Time taken for insertion sort with 100 elements in seconds: "+str(t2-t1))


for i in range(0,10000):
    a[i]=random.randint(1,100)

t1=time.time()
for i in range(1,10000):
    key = a[i]
    j=i-1
    while j>=0 and key<a[j]:
        a[j+1]=a[j]
        j-=1
    a[j+1]=key
t2=time.time()
f.write("\nTime taken for insertion sort with 10000 elements in seconds: "+str(t2-t1))

for i in range(0,100000):
    a[i]=random.randint(1,100)

t1=time.time()
for i in range(1,100000):
    key = a[i]
    j=i-1
    while j>=0 and key<a[j]:
        a[j+1]=a[j]
        j-=1
    a[j+1]=key
t2=time.time()
f.write("\nTime taken for insertion sort with 100000 elements in seconds: "+str(t2-t1))
f.close