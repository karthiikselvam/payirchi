def compareTriplets(a, b):
    ar = [0,0]
    newarr = list(zip(a,b))
    # [(1,3),(2,2),(3,1)]
    for i in range(len(newarr)):
        currenttup = newarr[i]
        if currenttup[0] > currenttup[1]:
            ar[0] += 1
        elif currenttup[0] < currenttup[1]:
            ar[1] += 1
        else :
            continue
    
    return ar


result = compareTriplets([1,2,3], [3,2,1])
print(result)