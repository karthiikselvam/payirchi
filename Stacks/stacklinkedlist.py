class Node:
    def __init__(self):
        self.data = None
        self.next = None

class Stack:
    
    def __init__(self):
        self.head = None

    def push(self,val):
        newNode = Node()
        newNode.data = val
        newNode.next = self.head
        self.head = newNode


    def pop(self):
        if self.head is None:
            print("Stack Underflow")
        else:
            tempval = self.head.val
            self.head = self.head.next
            return tempval

    def peek(self):
        if self.head is None:
            print("Stack Underflow")
        else:
            return self.head.data



