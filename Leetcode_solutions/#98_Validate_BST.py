# Problem: Validate Binary Search Tree
# LeetCode: #98
# Difficulty: Medium
# Time Complexity: O(n)
# Space Complexity: O(h)
# Approach: Pass valid range down — each node must fall within (min_val, max_val)
#           Left child gets max_val = current node
#           Right child gets min_val = current node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root,min_val = float('-inf'),max_val = float('inf')):
        if root is None:
            return True
        if not(min_val < root.val < max_val):
            return False
        return self.isValidBST(root.left,min_val,root.val) and self.isValidBST(root.right,root.val,max_val)         