arr = [1,2,3,4,4,5]
kdistance = 2 

for i in range(len(arr)-kdistance):
    for k in range(i+1,i+kdistance):
        if arr[i] == arr[k]:
            print(f"Yo boys duplicates exist and it is {arr[k]}")