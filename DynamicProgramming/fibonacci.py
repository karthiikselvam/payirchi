# fib (5) 
# Bottom up approach what we try to do is fill the table from bottom.
# Find the solution for the smaller problems 

def fibonacci(n):

    if (n == 1 or n == 2):
        return 1
    return fibonacci(n-1) + fibonacci(n-2)


result = fibonacci(5)
print(result)
