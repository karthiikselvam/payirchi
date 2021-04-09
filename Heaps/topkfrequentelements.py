from heapq import *

input = [1, 3, 5, 12, 11, 12, 11] 
k = 2
#output: [12, 11]

def topkfreqelements(inp,k):
    hashmap = {}
    
    for i in range(len(input)):
        if input[i] not in hashmap:
            hashmap[input[i]] = 1 
        else :
            hashmap[input[i]] += 1

    minheap = []
    for nums, freqs in hashmap.items():
        heappush(minheap,(freqs,nums))
        if len(minheap) > k :
            heappop(minheap)

    result = []
    while (minheap):
        result.append(heappop(minheap)[1])

    return result

out = topkfreqelements(input,k)
print(out)