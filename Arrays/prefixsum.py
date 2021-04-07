arr = [-1,2,1,-4,2,3,-1,2]
prefixsumdic = {}
sum = 0


for i in range(len(arr)):
    sum += arr[i] 
    if sum == 0 :
        print(f"Take it bro {0} to {i}")
    elif (sum in prefixsumdic):
        index = prefixsumdic[sum]
        print(f"Take it bro {index+1} to {i}")
    else :
        prefixsumdic[sum] = i

