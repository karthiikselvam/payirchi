import math
arr = [8,14,2,5,7,3,9,5]


minimum = math.inf
miniindex = -1
secondmax = -math.inf

for i in range(len(arr)):
    mini = arr[i]
    if mini < minimum:
        minimum = mini
        miniindex = i

for k in range(miniindex,len(arr)):
    secondmax = max(secondmax,arr[k])

profit = secondmax - minimum
print(profit)