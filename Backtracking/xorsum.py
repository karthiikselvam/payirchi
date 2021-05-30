ans = []
temp= []
nums=[1,3]        
def backtrack(nums,temp,start,end):
    ans.append(temp[:])
    for i in range(start,end):
        temp.append(nums[i])
        backtrack(nums,temp,i+1,end)
        temp.pop()
                
backtrack(nums,temp,0,len(nums))
print(ans)
sumof = 0
for li in ans:
    if (len(li) == 0):
        continue
    else:
        curxor = li[0]
        for ele in range(1,len(li)):
            curxor ^= ele
            sumof += curxor

print(sumof)
                
            
            