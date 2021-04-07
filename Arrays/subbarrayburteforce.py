arr = [-2,-3,4,-1,-2,1,5,-1]

maxsum = 0 

for i in range(len(arr)):
    sumtillnow = arr[i]
    for k in range(i+1, len(arr)):
        sumtillnow +=  arr[k]
        if sumtillnow > maxsum:
            maxsum = sumtillnow
        

print(maxsum)