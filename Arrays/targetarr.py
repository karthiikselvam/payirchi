def createTargetArray(nums, index):
        target = [-1] * len(index)
        for i in range(len(index)):
            if target[index[i]] == -1 :
                target[index[i]] = nums[i]
            else:
                temp = target[index[i]]
                nexttemp = -1
                target[index[i]] = nums[i]
                j = index[i] + 1
                while (j < len(target)):
                    if target[j] == -1:
                        target[j] = temp
                        break
                    else:
                        nexttemp = target[j]
                        target[j] = temp
                        temp = nextttemp
                        j += 1
        return target


result = createTargetArray([0,1,2,3,4], [0,1,2,2,1])
print(result)
