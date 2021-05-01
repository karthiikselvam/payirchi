value = [60,100,120]
weight = [10,20,30]
w = 50
n = len(weight)

memo = [ [-1 for i in range(w+1)]for j in range(n+1)]

def knapsack(value , weight , n, w):
    # base condition
    if(n == 0 or w == 0):
        return 0

    if (memo[n][w] != -1):
        return memo[n][w] 
    
    else :
        if ( weight[n-1] <= w):
            memo[n][w] =  max(value[n-1] + knapsack(value, weight, n-1, w-weight[n-1]), knapsack(value, weight, n-1, w))
            return memo[n][w]
       
        elif (weight[n-1] > w):
            memo[n][w] =  knapsack(value, weight, n-1, w)
            return memo[n][w]


result = knapsack(value, weight, n, w)
print(result)

