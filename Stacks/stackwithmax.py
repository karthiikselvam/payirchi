# Stack with Max : 
# Insertion 3 1 4 2 0

import math
class Stackwithmax:
    def __init__(self):
        self.stack = []
        self.maximum = -math.inf

    def push(self,item):
        if item > self.maximum:
            self.maximum = item
            self.stack.append((item,self.maximum))
        else :
            self.stack.append((item,self.maximum))

    def getmax(self):
        curr_val , max_val = self.stack.pop()
        return max_val

stack = Stackwithmax()
stack.push(3)
stack.push(1)
stack.push(4)
stack.push(2)
stack.push(0)
result = stack.getmax()
print(result)