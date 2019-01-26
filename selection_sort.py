import time
import random

f = open("selection-out.txt", "w")

a=[None]*100000

for i in range(0,100):
    a[i]=random.randint(1,100)

t1=time.time()
for i in range(0,100):
    min_element = i
    for j in range(i,100):
        if a[j]<a[min_element]:
            min_element=j
    temp=a[i]
    a[i]=a[min_element]
    a[min_element]=temp
t2=time.time()
f.write("Time taken for selection sort with 100 elements in seconds: "+str(t2-t1))

for i in range(0,10000):
    a[i]=random.randint(1,100)

t1=time.time()
for i in range(0,10000):
    min_element = i
    for j in range(i,10000):
        if a[j]<a[min_element]:
            min_element=j
    temp=a[i]
    a[i]=a[min_element]
    a[min_element]=temp
t2=time.time()
f.write("\nTime taken for selection sort with 10000 elements in seconds: "+str(t2-t1))

for i in range(0,100000):
    a[i]=random.randint(1,100)

t1=time.time()
for i in range(0,100000):
    min_element = i
    for j in range(i,100000):
        if a[j]<a[min_element]:
            min_element=j
    temp=a[i]
    a[i]=a[min_element]
    a[min_element]=temp
t2=time.time()
f.write("\nTime taken for selection sort with 100000 elements in seconds: "+str(t2-t1))
f.close

