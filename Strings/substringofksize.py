def countGoodSubstrings(s):
    charmap = {}
    sums = 0
    windowstart = 0
    for windowend in range(len(s)):
        rightchar = s[windowend]
        
        
        if rightchar not in charmap:
            charmap[rightchar] = 1
        else:
            charmap[rightchar] += 1
        
        if windowend >= 2:
            if(len(charmap)) == 3:
                sums += 1
                leftchar = s[windowstart]
                windowstart += 1
                if leftchar in charmap:
                    charmap[leftchar] -= 1
                    if charmap[leftchar] == 0:
                        del[charmap[leftchar]]
            else:
                leftchar = s[windowstart]
                windowstart += 1
                if leftchar in charmap:
                    charmap[leftchar] -= 1
                    if charmap[leftchar] == 0:
                        del[charmap[leftchar]]
    
    return sums

res = countGoodSubstrings("xyzzaz")
print(res)