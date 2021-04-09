from heapq import *

string = "Programming"
#Output: "rrggmmPiano"

def frequencysort(string):
    hashmap = {}
    for i in range(len(string)):
        if string[i] not in hashmap:
            hashmap[string[i]] = 1
        else :
            hashmap[string[i]] += 1
    maxheap = [] 
    for char , freq in hashmap.items():
        heappush(maxheap,(-freq,char))

