value = [60,100,120]
weight = [10,20,30]
w = 50
# output = 220
n = len(weight)

def knapsack(value , weight , n, w):
    # base condition
    if(n == 0 or w == 0):
        return 0
    elif ( weight[n-1] <= w):
        return max(value[n-1] + knapsack(value, weight, n-1, w-weight[n-1]), knapsack(value, weight, n-1, w))

    else :
        return knapsack(value, weight, n-1, w)


result = knapsack(value, weight, n, w)
print(result)

