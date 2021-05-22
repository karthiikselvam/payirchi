arr = [5,3,1,7,6,4,2,3]
target = 14
windowsum = 0

startptr = 0 
endptr   = 0 

while(endptr < len(arr)):
    windowsum += arr[endptr]

    if windowsum > target:
        windowsum -= arr[startptr]
        startptr += 1
        if windowsum == target:
            print(startptr,endptr)
            break
        endptr += 1

    if windowsum == target:
        print(startptr,endptr)
        break
    
    endptr += 1
