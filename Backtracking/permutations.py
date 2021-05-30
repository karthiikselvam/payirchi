def permutations(nums,buffer,startindex,bufferindex,result):
    if (bufferindex == len(nums)):
        result.append(list(buffer)) 
        return 
           
    if (startindex == len(nums)):
        return 
           
    for i in range(startindex,len(nums)):   
        buffer[i] = nums[i]
        permutations(nums,buffer,startindex+1,bufferindex+1,result)               
        
    
         
result = []
buffer = [-1,-1,-1]
startindex = 0
bufferindex = 0 
nums = [1,2,3]
permutations(nums,buffer,startindex,bufferindex,result)
print(result)