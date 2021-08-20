arr = [1,2,3]
start = 0
end   = len(arr) - 1


def swap( start , end ):
    temp = arr[start]
    arr[start] = arr[end]
    arr[end]   = temp

def reverse(arr):
    global start
    global end
    while( start <= end ) :
        swap(start,end)
        start += 1
        end   -= 1


reverse(arr)
print(arr)
