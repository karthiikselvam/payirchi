class Node :
    def __init__(self,val = 0):
        self.next = None
        self.val  = val

def reversal(head):
    current = head
    previous = None
    while(current != None):
        next = current.next
        current.next = previous
        previous = current
        current = next
    return previous

first = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)

first.next = second
second.next = third
third.next = fourth
head = first

result = reversal(head)

while(result != None):
    print(result.val)
    result = result.next