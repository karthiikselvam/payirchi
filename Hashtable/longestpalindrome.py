def longestPalindrome(s: str) -> int:

    hashmap = {}
    length = len(s)

    for i in range(len(s)):
        if s[i] not in hashmap:
            hashmap[s[i]] = 1
        else:
            hashmap[s[i]] += 1

    sumofhashmap = 0
    for key in hashmap:
        if hashmap[key] % 2 == 0:
            sumofhashmap += hashmap[key]

    if sumofhashmap == 0:
        return 1
    elif sumofhashmap == length:
        return sumofhashmap
    else:
        return sumofhashmap + 1

result = longestPalindrome("abccccdd")
print(result)