import time
import random

f = open("bubble-out.txt", "w")

a=[None]*100000

for i in range(0,100):
    a[i]=random.randint(1,100)
t1=time.time()

for i in range(0,99):
    for j in range(0,99-i):
        if a[j]>a[j+1]:
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp
t2=time.time()
f.write("Time taken for bubble sort with 100 elements in seconds: "+str(t2-t1))

for i in range(0,10000):
    a[i]=random.randint(1,100)
t1=time.time()

for i in range(0,9999):
    for j in range(0,9999-i):
        if a[j]>a[j+1]:
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp
t2=time.time()
f.write("\nTime taken for bubble sort with 10000 elements in seconds: "+str(t2-t1))

for i in range(0,100000):
    a[i]=random.randint(1,100)
t1=time.time()

for i in range(0,99999):
    for j in range(0,99999-i):
        if a[j]>a[j+1]:
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp
t2=time.time()
f.write("\nTime taken for bubble sort with 100000 elements in seconds: "+str(t2-t1))
f.close

