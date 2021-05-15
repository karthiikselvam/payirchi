arr  = [18,7,6,12,15]
#output = [-1,12,12,15,-1]

def nextGreatestElement(arr):
    nextgreatelemenlist = [-1 for i in range(len(arr))]
    stack = []
    stack.append(0)

    for k in range(1, len(arr)):
        while len(stack) != 0 and arr[k] >  arr[stack[-1]]:
            index = stack.pop()
            nextgreatelemenlist[index] = arr[k]

        if arr[k] <= arr[stack[-1]]:
            stack.append(k)

    return nextgreatelemenlist



result = nextGreatestElement(arr)