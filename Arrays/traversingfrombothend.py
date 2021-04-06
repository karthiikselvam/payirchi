arr = [1,2,3,4,5,6,7,8,9,10]

start = 0
end = len(arr)-1

def swap(arr,start,end):
    temp = arr[start]
    arr[start] = arr[end]
    arr[end] = temp


while(start < end):
    swap(arr,start,end)
    start += 1
    end -= 1

for i in range(len(arr)):
    print(arr[i])