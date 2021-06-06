# [1,3]
# [] , [1] ,[3] , [1,3]

def subset(arr,result):
    result.append([])
    for i in range(len(arr)):
        for j in result:
            #copy the list and append
            newlist = list(j)
            newlist.append(arr[i])
            
        result.append(newlist)
    
    return result 

result = []
result = subset([1,3],result)
print(result)

