n = 5
for i in range(n,0,-1):
    for k in range(n-i,0,-1):
        print(" ",end="")

    for j in range(i,0,-1):
        print("*",end="")

    print("\r")


