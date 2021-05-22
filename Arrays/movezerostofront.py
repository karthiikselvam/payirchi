arr = [2,4,0,3,0,1,0]
# output = [0,0,0,2,4,1,3]


def movezerostofront(arr):
    boundary = -1
    start   = 0
    
    while (start < len(arr)):
        if arr[start] == 0:
            boundary  += 1
            arr[boundary] , arr[start] = arr[start] , arr[boundary] 
            start += 1
        else:
            start += 1

    return arr

result = movezerostofront(arr)
print(result)