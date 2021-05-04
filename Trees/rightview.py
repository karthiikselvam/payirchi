from collections import deque
class Node :
    def __init__(self,val ):
        self.left = None
        self.right = None
        self.val = val


def traversal(root):
    if root :
        print(root.val, end=" ")

        if root.left:
            traversal(root.left)
        
        if root.right:
            traversal(root.right)

def rightview(root):
    queue = deque()
    if not root:
        return "Root Doesn't Exist"

    queue.append(root)
    while(queue):
        levelsize = len(queue)
        for i in range(len(queue)):
            current_node = queue.popleft()

            if i == levelsize - 1:
                print(current_node.val, " ")

            if current_node.left :
                queue.append(current_node.left)

            if current_node.right:
                queue.append(current_node.right)

            

node1= Node(1)
node2= Node(2)
node3= Node(3)
node4= Node(4)
node5= Node(5)
node6= Node(6)
node7= Node(7)
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7

#traversal(node1)
rightview(node1)