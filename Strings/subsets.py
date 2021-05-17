
def subsets(s, output):

    if len(s) == 0:
        print(output)
        return
    
    op1 = output
    op2 = output
    op2 += s[0]
    s = s.replace(s[0],"")
    subsets(s, op1)
    subsets(s, op2)
    return






if __name__ == "__main__":
    s = "abc"
    output = ""
    subsets(s,output)