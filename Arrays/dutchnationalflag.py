arr =  [1,4,5,4,4,6,2,3]
#           i 
lowerBoundary = 0
higherBounary = len(arr) - 1
pivot = 4
i = 0

def swap(arr , i , boundary):
    temp = arr[i]
    arr[i] = arr[boundary]
    arr[boundary] = temp

while(i <= higherBounary):
    if(arr[i] < pivot):
        swap(arr , i , lowerBoundary)
        i += 1
        lowerBoundary += 1
    elif(arr[i] > pivot):
        swap(arr,i,higherBounary)
        higherBounary -= 1
    else :
        i += 1

for k in range(len(arr)):
    print(arr[k])