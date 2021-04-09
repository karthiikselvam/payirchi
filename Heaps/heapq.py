from heapq import *

heap = [10,230,22,39,223]

def heaptest(heap):
    print(f"Current elements {heap}")
    heapify(heap)
    print(f"After heapify {heap}")
    heappop(heap)
    heappush(heap, 1)
    print(f"After pushing elements {heap}")
heaptest(heap)