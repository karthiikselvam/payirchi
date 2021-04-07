arr =  [5,3,1,7,6,4,2,3]
target = 0
windowStart = 0
windowSum = 0

for windowEnd in range(len(arr)):
    windowSum  +=  arr[windowEnd] 

    if windowSum > target :
        windowSum = windowSum - arr[windowStart] 
        windowStart += 1

    if windowSum == target:
        print("Target is in present in the array {}".format(windowSum)) 
        print(f"okay its present {windowSum}")
        break
