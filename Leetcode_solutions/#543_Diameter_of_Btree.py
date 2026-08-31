# Problem: Diameter of Binary Tree
# LeetCode: #543
# Difficulty: Easy
# Time Complexity: O(n)
# Space Complexity: O(h)
# Approach: Recursive — calculating diameter for every node

class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

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

# test cases
tree_tuple1 = ((4,2,5),1,3)
tree_tuple2 = (2,1,None)
tree_tuple3 = (None)

tree1 = parse_tuple(tree_tuple1)
tree2 = parse_tuple(tree_tuple2)
tree3 = parse_tuple(tree_tuple3)
 
def diameter(node):
    max_diameter = [0]
    def dfs(node):
        if node is None:
            return -1
        left_height = dfs(node.left)    
        right_height = dfs(node.right)
        max_diameter[0] = max(max_diameter[0],left_height + right_height + 2)
        return 1 + max(left_height,right_height)
    dfs(node)    
    return max_diameter[0]    

print(diameter(tree1))    
print(diameter(tree2))    
print(diameter(tree3))    






            

           