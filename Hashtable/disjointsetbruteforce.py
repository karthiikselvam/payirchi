set1 = [1,2,3,4,5]
set2 = [7,8,9,6,5]


def disjointSet(set1,set2):
    
    for i in range(len(set1)):
        for k in range(len(set2)):
            if set1[i] == set2[i]:
                return "Set is not Disjoint"

    
    return "Set is Disjoint"

result = disjointSet(set1 , set2)
print(result)