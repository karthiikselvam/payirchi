def peakelement(arr):
    start = 0 
    end   = len(arr)-1 

    while (start <= end): 
        mid = (start + end) // 2 
        if mid >= 0 and arr[mid-1] < arr [mid] and arr[mid] > arr[mid+1]: 
            return mid 
        if arr[mid-1] > arr[mid]: 
            end =  mid - 1 
        else: 
            start = mid  + 1


result = peakelement([3,4,5,1])
print(result)

