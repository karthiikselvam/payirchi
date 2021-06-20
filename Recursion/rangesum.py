class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right= None

def rangesum(root,low,high):
    if root is None:
        return 0
    
    if root.val <= high and root.val >= low:
        return root.val + rangesum(root.left,low,high) + rangesum(root.right,low,high)
    else:
        return 0
        
        
low = 7
high = 15



node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

node1.val = 10
node2.val = 5
node3.val = 15
node1.left = node2
node1.right= node3

result = rangesum(node1,low,high)
print(result)
