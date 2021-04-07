arr = [2,4,0,3,0,1,0]
#output = [2,4,3,1,0,0,0]


boundary = len(arr) - 1
i = 0

def swap(arr , i , boundary):
    temp = arr[i]
    arr[i] = arr[boundary]
    arr[boundary] = temp

while(i < boundary):
    if (arr[i]==0):
        swap(arr,i,boundary)
        boundary -= 1
        i -= 1
    else:
        i += 1


for k in range(len(arr)):
    print(arr[k])