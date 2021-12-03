arr = [ 1, 2, 3 ] 

dic = { 1 : "a",
        2 : "b"}

for i in range(len(arr)-1):
    if arr[i] in dic :
        print(dic[arr[i]])

