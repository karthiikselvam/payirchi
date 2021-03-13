"""
Given ‘N’ ropes with different lengths, we need to connect these ropes into one 
big rope with minimum cost. The cost of connecting two ropes is equal to the sum 
of their lengths.
Input: [1, 3, 11, 5]
Output: 33
Explanation: First connect 1+3(=4), then 4+5(=9), and then 9+11(=20). So the total cost is 33 (4+9+20)
"""
from heapq import *
def connect_ropes(arr):

    minheap = []
    for i in range(len(arr)):
        heappush(minheap,arr[i])
    sumofminsresults = []
    while len(minheap) > 1:
        firstmin = heappop(minheap)
        secondmin = heappop(minheap)
        sumofmins = firstmin + secondmin
        sumofminsresults.append(sumofmins)
        heappush(minheap,sumofmins)

    return sum(sumofminsresults)

result = connect_ropes([3, 4, 5, 6])
print(result)
