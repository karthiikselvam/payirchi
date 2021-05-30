def backtrack(start, end, tmp,nums):
    ans.append(tmp[:])
    for i in range(start,len(nums)):
        tmp.append(nums[i])
        backtrack(i+1, end, tmp, nums)
        tmp.pop()


ans = []
nums = [1,2,3]
backtrack(0, len(nums), [],nums)
print(ans)