arr = [2,4,6,8,10,12,14]
#output = [2,6,12,20,30,42,56]

prefixsum = []

for i in range(len(arr)):
    prefixsum.append(-1)    

prefixsum[0] = arr[0]


for i in range(1, len(arr)):
    prefixsum[i] = prefixsum[i-1] + arr[i]

print(prefixsum)
