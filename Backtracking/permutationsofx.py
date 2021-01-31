# Given an array A, print all permutations of size X.
arr = [1,2,3] 
# [1,2] [2,1] [1,3] [3,1] [2,3] [3,2]
buffer = [None,None]
isinbuffer = [False,False,False]

def permutations(arr,buffer,buffer_index,isinbuffer):

    if len(buffer) == buffer_index:
        print(buffer)
        return


    for i in range(0,len(arr)):
        if (not isinbuffer[i]):
            buffer[buffer_index] = arr[i]
            isinbuffer[i]= True
            permutations(arr,buffer,buffer_index+1,isinbuffer)
            isinbuffer[i] = False

permutations(arr,buffer,0,isinbuffer)