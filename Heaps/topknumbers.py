from heapq import *

def GiveMeTopKNumbers(arr,k):
   minheap = []
   for i in range(k):
       minheap.append(arr[i])

   for l in range(k , len(arr)):
       if arr[l] > minheap[0]:
           heappop(minheap)
           heappush(minheap,arr[l])

   return minheap



input=[3, 1, 5, 12, 2, 11] 
k = 3
result = GiveMeTopKNumbers(input,k)
print(result)
    
