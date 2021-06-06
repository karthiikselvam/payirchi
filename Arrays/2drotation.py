def findRotation(mat, target):
        
        def rotate(mat) :
            rows = len(mat)  
            cols = len(mat) 
            
            temp = [[0 for i in range(cols)] for j in range(rows)]
            
            colsize = cols - 1     
            for i in range(rows):
                for j in range(cols):
                    temp[j][colsize] = mat[i][j]
                    
                colsize  -= 1
            
            return temp

        def check(rotatedmatx,target):
            for i in range(len(rotatedmatx)):
                for j in range(len(rotatedmatx[0])):
                    if rotatedmatx[i][j]   != target[i][j]:
                        return False
            return True    
        
        currentmat = mat 
        
        for i in range(4):
            rotatedmatx = rotate(currentmat)
            if (check(rotatedmatx , target)):
                return True
            else:
                currentmat = rotatedmatx
        
        return False

mat = [[0,0,0],[0,1,0],[1,1,1]]
target = [[1,1,1],[0,1,0],[0,0,0]]
result = findRotation(mat, target)             
print(result)