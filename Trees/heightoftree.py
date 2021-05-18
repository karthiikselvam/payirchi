class BinaryTree:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val   = val


def height(node):

    if node is None :
        return 0
    
    if node.left is None and node.right is None :
        return 1
        
    leftheight = height(node.left)
    
    rightheight = height(node.right)

    return 1 + max(leftheight,rightheight)


node1 = BinaryTree(1)
node2 = BinaryTree(2)
node3 = BinaryTree(3)
node4 = BinaryTree(4)

node1.left = node2
node1.right = node3
node2.left = node4

result = height(node1)
print(result)