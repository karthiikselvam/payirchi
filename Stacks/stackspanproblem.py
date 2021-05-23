# https://www.geeksforgeeks.org/the-stock-span-problem/
arr = [100, 80, 60, 70, 60, 75, 85]
# output  = [1, 1, 1, 2, 1, 4, 6]


def stockSpan(arr):

    result = [1] * len(arr)

    for i in range(1,len(arr)) :
        count = 0
        j = i - 1
        
        while True :
            if arr[j] < arr[i]:
                count += 1
                j -= 1
            else:
                break
        
        result[i] += count

    return result

result = stockSpan(arr)
print(result)
    