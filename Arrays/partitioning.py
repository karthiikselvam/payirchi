arr = [2,4,0,3,0,1,0]
# output = [0,0,0,2,4,3,1]

newarr = []

for i in range(len(arr)):
    if (arr[i] == 0 ):
        newarr.append(0)

for k in range(len(arr)):
    if(arr[k] != 0):
        newarr.append(arr[k])


[print(newarr[i]) for i in range(len(newarr))]