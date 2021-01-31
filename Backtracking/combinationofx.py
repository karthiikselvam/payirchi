# Given an array of integers, print all combinations of size X.

def combinations(arr,arr_index,buffer,buffer_index):

    if buffer_index == len(buffer):
        print(buffer)
        return

    if len(arr) == arr_index :
        return

    for i in range(arr_index,len(arr)):
        buffer[buffer_index] = arr[i]
        combinations(arr,i+1,buffer,buffer_index+1)

arr = [1,2,3]
buffer = [None,None]
combinations(arr,0,buffer,0)