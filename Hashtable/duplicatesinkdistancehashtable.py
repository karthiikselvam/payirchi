arr = [1,2,3,4,4,5]
kdistance = 2 

hashmap = {}
start = 0

def getKey(start, hashmap):
    for key , value in hashmap.items():
        if value == start:
            return key

for i in range(len(arr)):
    
    if len(hashmap) >= kdistance:
        if start in hashmap.values():
            key = getKey(start, hashmap)
            del hashmap[key]
            start += 1
   
    if arr[i] in hashmap :
        print(f"Bro diplicate exist and it is {arr[i]}")
        break
    else:
        hashmap[arr[i]] = i