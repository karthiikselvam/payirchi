# Maximal Matching on fly.

def maximal_matching(word):
    n = len(word)
    f = [0] * n
    k = 0
    for i in range(1,n):
        while(word[i] != word[k] and k>0):
            k = f[k-1]
        if word[i] == word[k]:
            k += 1
        f[i] = k
    return f

word = "abaababaa"
result = maximal_matching(word)
print(result)