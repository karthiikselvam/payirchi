class Node:
    def __init__(self,val=None):
        self.val = val
        self.next = None


def reverseLL(head):
    previous = None
    nextptr  = None  
    current  = head
    
    while(current != None):
        nextptr = current.next
        current.next = previous
        previous   = current
        current = nextptr
    
    while previous:
        print(previous.val,end= "")
        previous = previous.next




node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)


node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

head = node1
reverseLL(head)
