matrix = [[1,2,1,4,8],
          [3,7,8,5,1],
          [8,7,7,3,1],
          [8,1,2,7,9]
          ]

norows = len(matrix) 
nocols = len(matrix[0])

def printCommonElements(matrix):
    mp = dict()

    for i in range(nocols):
        mp[matrix[0][i]] = 1

    
    for j in range(1,norows):
        for k in range(nocols):

            if( matrix[j][k] in mp.keys() and mp[matrix[j][k]] == j):
                mp[matrix[j][k]] = j + 1
                if ( j == (norows-1)):
                    print(matrix[j][k] , end = " ")

printCommonElements(matrix)

