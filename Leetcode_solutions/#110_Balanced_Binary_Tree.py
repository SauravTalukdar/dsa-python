# Problem: Balanced Binary Tree
# LeetCode: #110
# Difficulty: Easy
# Time Complexity: O(n) — visits every node once
# Space Complexity: O(h) — recursion call stack
# Approach: Recursive nested function returns (is_balanced, height)
#           outer function extracts only balanced status with [0]
# Key insight: height calculated as side effect — no separate traversal needed

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root):
        def check(root):
            if root is None:
                return True,0
            balanced_l,height_l = check(root.left)    
            balanced_r,height_r = check(root.right)
            balanced = balanced_l and balanced_r and abs(height_l - height_r) <=1
            height = 1 + max(height_l,height_r)
            return balanced,height
        return check(root)[0]





        