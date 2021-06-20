def RevString(string,length):
    startptr = 0 
    endptr   = length - 1

    while startptr < endptr :

        temp = string[endptr]
        string[endptr] = string[startptr]
        string[startptr] = temp
        startptr += 1
        endptr   -= 1

    return string





s = 'getting good at coding needs a lot of practice'
string = s.split(' ')
string = RevString(string,len(string))
print(" ".join(string))
