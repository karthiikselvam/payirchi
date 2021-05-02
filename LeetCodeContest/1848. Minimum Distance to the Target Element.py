# 1848. Minimum Distance to the Target Element
def getMinDistance(nums,target,start):
    i = start
    if (nums[i] == target ):
        return abs(i-start)

    foundforward = False    
    forwardindex = 0
    for i in range(i,len(nums)):
        if nums[i] != target:
            continue
        else :
            foundforward = True
            forwardindex = i
            break
    if foundforward:
        sol1 = abs(forwardindex - start)
        
    foundbackward = False
    backwardindex = 0
    i = start
    for k in range(i,-1,-1):
        if nums[k]!= target:
            continue
        else:
            foundbackward = True
            backwardindex = k
            break

    if foundbackward:    
        sol2 = abs(backwardindex - start)
        
    if foundforward and foundbackward:
        return min(sol1,sol2)
    elif foundforward:
        return sol1
    elif foundbackward:
        return sol2

result = getMinDistance([5,3,6],5,2)
print(result)