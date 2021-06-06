from heapq import *

def find_kth_smallest(lists,k):
    minheap = []
    
    for i in range(len(lists)):
        heappush(minheap,(lists[i][0],0,lists[i]))
        
    numbercount , number = 0, 0
    while minheap:
        number , i ,list = heappop(minheap)
        numbercount += 1
        if numbercount == k:
            break
        
        if len(list) > i+1:
            heappush(minheap,(list[i+1],i+1,list))
            
    
    return number
    

def main():
    print(str(find_kth_smallest([[2,6,8,],[3,6,7],[1,3,4]],5)))
    
main()