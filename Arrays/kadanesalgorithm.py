arr = [-2,-3,4,-1,-2,1,5,-1]

maxsumtillhere = 0
maxsumsofar = 0

for i in range(len(arr)):
    maxsumtillhere = max(0, maxsumtillhere + arr[i])
    maxsumsofar = max(maxsumtillhere,maxsumsofar)

print(maxsumsofar)


