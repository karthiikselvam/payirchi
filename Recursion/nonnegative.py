def nonnegsum(n):
    if n > 0 and n == 1:
        return 1

    return n + nonnegsum(n-1)


n = 5
result = nonnegsum(n)
print(result)



