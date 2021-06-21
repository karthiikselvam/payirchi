parenthesis = ['(' , '{' , '[']
inputstring = "()](()[()])"
maping = {')':'(', ']':'[','}':'{'}
stack = []

flag = True
for char in inputstring:
    if char in parenthesis:
        stack.append(char)
    else :
        if stack:
            topelement = stack.pop()
            mapingelement = maping[char]
            if topelement != mapingelement:
                flag = False 
                print("Not Balanced")
                break
        else:
            flag = False 
            print("Not Balanced")
            break

if flag:    
    print("balanced")

