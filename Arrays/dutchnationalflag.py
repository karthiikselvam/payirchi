arr = [2,0,2,1,1,0]
#output = [0,0,1,1,2,2]

pivot = 1 
startboundary = -1
endboundary   = len(arr)
i = 0 

def swap( arr, i , boundary ):
    temp = arr[i] 
    arr[i] = arr[boundary]
    arr[boundary] = temp

while( i < endboundary ) :

    if(arr[i] < pivot) :
        startboundary += 1
        swap(arr,i,startboundary)
        i += 1
    elif( arr[i] > pivot):
        endboundary -= 1
        swap(arr, i , endboundary)
    else:
        i += 1


print(arr)
