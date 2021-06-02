class LL:
    def __init__(self,data):
        self.val = data
        self.next = None


def intersection(node3,node10):
    reset = node10
    while node3:
        val = node3.val

        while node10:

            if(node10.val == val):
                return val
            else:
                node10 = node10.next
        
        node10 = reset
        node3  = node3.next

    return "No Intersection"


node3 = LL(3)
node6 = LL(6)
node9 = LL(9)
node10= LL(10)
node15= LL(15)
node30= LL(30)

node3.next = node6
node6.next = node9
node9.next = node15
node15.next = node30
node10.next = node15

result = intersection(node3,node10)
print("Node Intersection point is " + str(result))

