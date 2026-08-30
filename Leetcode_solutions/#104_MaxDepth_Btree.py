# Problem: Maximum Depth of Binary Tree
# LeetCode: #104
# Difficulty: Easy
# Time Complexity: O(n) — visits every node once
# Space Complexity: O(h) — h is height of tree, recursion call stack
# Approach: Recursive,height of node = 1 + max(left height, right height)
# Base case: empty node returns -1

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

def traverse_height(node):
    if node is None:
        return -1   
    # left_height = traverse_height(node.left) 
    # right_height = traverse_height(node.right)
    return 1 + max(traverse_height(node.left),traverse_height(node.right)) #we can pass the left_height and right_height or 
                                                                            #pass it like this  

print(traverse_height(tree))    
            

           