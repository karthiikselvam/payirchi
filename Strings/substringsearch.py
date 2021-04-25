# input = ABACADABRAC pattern = ABRA
# output= Substring is present 


def substring(givenstring , pattern):
    length1 = len(givenstring)
    length2 = len(pattern)

    for index in range(0,length1-length2):
        for i in range(0,length2):
            if pattern[i] != givenstring[index + i]:
                break
        
        if length2-1 == i:
            return "Bro substring is present"

    return "Substring not present"

result = substring("ABACADABRAC", "ABRAa")
print(result)