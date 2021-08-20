arr = [2,0,2,1,1,0]
# output = [0,0,2,2,1,1]

boundary = -1 
i = 0 

def swap( i , boundary, arr ) :
    temp = arr[i]
    arr[i] = arr[boundary]
    arr[boundary] = temp

while( i < len(arr) ) : 
    if arr[i] == 0 :
        boundary += 1
        swap(i,boundary, arr)
    i += 1


print(arr)
