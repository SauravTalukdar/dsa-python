# Problem: Insert into a Binary Search Tree
# LeetCode: #701
# Difficulty: Medium
# Time Complexity: O(h) — h is height of tree, O(log n) balanced, O(n) worst case
# Space Complexity: O(h) — recursion call stack
# Approach: Recursive — compare val with current node, go left if smaller, right if larger
#           create new node when None, return node up to connect

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insertIntoBST(self, root, val: int):
        if root is None:
            root = TreeNode(val)
        elif val < root.val:
            root.left = self.insertIntoBST(root.left,val)
        elif val > root.val:
            root.right =  self.insertIntoBST(root.right,val)
        return root 

solution = Solution()

#test cases
#1.
tree = solution.insertIntoBST(None,4)
tree = solution.insertIntoBST(tree,2)
tree = solution.insertIntoBST(tree,7)
tree = solution.insertIntoBST(tree,1)
tree = solution.insertIntoBST(tree,3)
tree = solution.insertIntoBST(tree,5)

#2.
tree1 = solution.insertIntoBST(None,40)
tree1 = solution.insertIntoBST(tree1,20)
tree1 = solution.insertIntoBST(tree1,60)
tree1 = solution.insertIntoBST(tree1,10)
tree1 = solution.insertIntoBST(tree1,30)
tree1 = solution.insertIntoBST(tree1,50)
tree1 = solution.insertIntoBST(tree1,25)


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

# display_keys(tree)    
# display_keys(tree1)    
   
        