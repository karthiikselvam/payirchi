def maxValue(n: str, x: int) -> str:
        
    def callpos(n,x):
        n = list(n)
        
        for i in range(len(n)):
            if int(n[i]) > x:
                continue 
            else:
                n.insert(i,str(x))
                return ''.join(n)
                break
                
    def callneg(n,x):
        n = list(n)
        for i in range(len(n)-1,0,-1):
            if int(n[i]) > x:
                continue
            else:
                n.insert(i+1,str(x))
                print(n)
                return ''.join(n)
                break
        
        
    if int(n) > 0:
        res = callpos(n,x)
        return res
    else:
        res = callneg(n,x)
        return res

res = maxValue("-13", 2)
print(res)