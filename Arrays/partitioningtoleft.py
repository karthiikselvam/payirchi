arr = [2,4,0,3,0,1,0]
# output = [0,0,0,2,4,3,1]

boundary = 0

def swap(arr, i ,boundary):
    temp = arr[i]
    arr[i] = arr[boundary]
    arr[boundary] = temp

for i in range(len(arr)):
    if (arr[i] == 0):
        swap(arr , i , boundary)
        boundary += 1

for k in range(len(arr)):
    print(arr[k])