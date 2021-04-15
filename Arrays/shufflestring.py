from heapq import *

def restoreString(s, indices):
    
        
    out = []    
    arr = []
    for k in range(len(indices)):
        arr.append((indices[k],s[k]))
    
    minheap = []
        
    for i in range(len(arr)):
        heappush(minheap,arr[i])
            
    while minheap:
        item = heappop(minheap)
        reqitem = item[1]
        out.append(reqitem)
    
    return ''.join(out)

result = restoreString("codeleet",[4,5,6,7,0,2,1,3])
print(result)