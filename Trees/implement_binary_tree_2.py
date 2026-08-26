class TreeNode:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None

# node0 = TreeNode(2)        
# node1 = TreeNode(3)        
# node2 = TreeNode(1)        
# node3 = TreeNode(5)        
# node4 = TreeNode(3)        
# node5 = TreeNode(4)        
# node6 = TreeNode(7)        
# node7 = TreeNode(6)        
# node8 = TreeNode(8)

# node0.left = node1
# node1.left = node2
# node0.right = node3
# node3.left = node4
# node4.right = node5
# node3.right = node6
# node6.left = node7
# node6.right = node8 ,this is very inconvinient to manually connect nodes

#better method,we can create a tuple

tree_tuple = ((1,3,None),2,((None,3,4),5,(6,7,8))) #this can represent a tree structure. (leftnode,key,rightnode)

def parse_tuple(data): #this takes a tuple like the above one
    if isinstance (data,tuple) and len(data) == 3: #checks if the data passed is a tuple and length is 3(left,key,right)
        node = TreeNode(data[1])
        node.left = parse_tuple(data[0])
        node.right = parse_tuple(data[2])
    elif data is None:
        node = None
    else:
        node = TreeNode(data)
    return node

tree = parse_tuple(tree_tuple)
print(tree.key)
print(tree.left.key,tree.right.key)
print(tree.left.left.key,tree.left.right,tree.right.left.key,tree.right.right.key)
print(tree.right.left.right.key,tree.right.right.left.key,tree.right.right.right.key)



