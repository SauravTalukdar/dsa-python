# Problem: Minimum Depth of Binary Tree
# LeetCode: #111
# Difficulty: Easy
# Time Complexity: O(n)
# Space Complexity: O(h)
# Approach: Recursive — if one child is None take max (skewed tree case)
#           if both children exist take min (normal case)
# Key insight: None side is not a valid leaf path — must use max to avoid it

class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

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

#test cases
tree_tuple1 = ((1,3,None),2,((None,3,4),5,(6,7,8)))
tree_tuple2 = (None,2,(None,3,(None,4,(None,5,6))))
tree_tuple3 = (None)    
tree_tuple4 = ((4,2,5),1,3)    

#making trees
tree1 = parse_tuple(tree_tuple1)
tree2 = parse_tuple(tree_tuple2)
tree3 = parse_tuple(tree_tuple3)
tree4 = parse_tuple(tree_tuple4)


def minDepth(root):
    if root is None:
        return 0
    if root.left is None or root.right is None:
        return 1 + max(minDepth(root.left),minDepth(root.right))
    else:
        return 1 + min(minDepth(root.left),minDepth(root.right))

print(minDepth(tree1))        
print(minDepth(tree2))        
print(minDepth(tree3))        
print(minDepth(tree4))        
