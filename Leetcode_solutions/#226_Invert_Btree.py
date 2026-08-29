# Problem: Maximum Depth of Binary Tree
# LeetCode: #104
# Difficulty: Easy
# Time Complexity: O(n) — visits every node once
# Space Complexity: O(h) — h is height of tree, recursion call stack
# Approach: Recursive,swapping the variables and calling recursion on both left and right nodes
# Base case: empty node returns None

class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

tree_tuple = ((1,3,None),2,((None,3,4),5,(6,7,8)))

def parse_tuple(data):
    if isinstance (data,tuple) and len(data) == 3:
        node = TreeNode(data[1])
        node.left = parse_tuple(data[0])
        node.right = parse_tuple(data[2])
    elif data is None:
        node = None   
    else:
        node = TreeNode(data)   
    return node

tree = parse_tuple(tree_tuple)

def display_keys(node,space='\t',level=0):
    if node is None:
        print(space*level + 'Ø')
        return
    if node.left is None and node.right is None:
        print(space*level + str(node.val))
        return
    display_keys(node.right,space,level+1)
    print(space*level + str(node.val))
    display_keys(node.left,space,level+1)

def invert(node):
    if node is None:
        return None
    node.left ,node.right = node.right,node.left
    invert(node.left)            
    invert(node.right) 
    return node

display_keys(tree)
a = invert(tree)
display_keys(a)
            

           