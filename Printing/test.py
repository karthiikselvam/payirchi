import math
n=int(input())
a=input()
a=a.split()
lst=[]
w=[]
sum=0
for i in range(len(a)):#converting from char to integer format
    g=int(a[i])
    lst.append(g)
sum 
indx = - 1 
val  = math.inf
for i in range(len(lst)):

    sumofarr = sum(lst) - lst[i]
    if sumofarr % 7 == 0 :
        if lst[i] <= val :
            val = lst[i]
            indx = i

print(indx)
       