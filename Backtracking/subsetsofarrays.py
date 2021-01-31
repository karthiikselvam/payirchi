def get_array(buffer,buffer_index,result):
    current_list = []
    for i in range(buffer_index):
        current_list.append(buffer[i])
    
    result.append(current_list)

def subsets_on_fly(arr,arr_index,buffer,buffer_index,result):

    get_array(buffer,buffer_index,result)

    if buffer_index == len(buffer):
        return 

    if arr_index == len(arr):
        return 

    for i in range(arr_index,len(arr)):
        buffer[buffer_index] = arr[i]
        subsets_on_fly(arr,i+1,buffer,buffer_index+1,result)        

    return result

result = []
arr  = [1,2,3]
buffer = [None,None,None]
r = subsets_on_fly(arr,0,buffer,0,result)
print(r)