class Stack:
    def __init__(self,limit = 10):
        self.stack = []
        self.limit = limit


    def push(self,element):
        if len(self.stack) > self.limit:
            return "Stack overflow"
        else:
            self.stack.append(element)

    def pop(self):
        if len(self.stack) <= 0:
            print("Stack Underflow")
        else: 
            return self.stack.pop()

    def peek(self):
        if len(self.stack) <= 0:
            return "Stack Underflow"
        else:
            return self.stack[-1]
    
    def __str__(self):
        return f'{self.stack}'


stack = Stack(20)
stack.push(10)
stack.push(20)
print(stack)
stack.pop()
stack.pop()
stack.pop()
stack.pop()



