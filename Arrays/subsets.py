arr = [1,2,3]
# [] , [1] , [2] , [3] , [1,2] , [1,3] , [2,3] , [1,2,3]



def subsets(arr):

    counter = pow(2, len(arr))

    result = []
    for count in range(0,counter):
        tempresult = [] 
        for j in range(len(arr)):
            if(count & (1 << j) > 0):
                tempresult.append(arr[j])
        if len(tempresult) == 2:
            result.append(tempresult)

    return result

result = subsets(arr)
print(result)
