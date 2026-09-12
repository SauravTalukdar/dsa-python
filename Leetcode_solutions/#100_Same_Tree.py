# Problem: Same Tree
# LeetCode: #100
# Difficulty: Easy
# Time Complexity: O(n) — visits every node once
# Space Complexity: O(h) — recursion call stack
# Approach: Recursive — check if both None, one None, or values equal
#           then recursively check left and right subtrees
# Key insight: two trees are same if structure AND values match at every node

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None: #structure same
            return True  
        if p is None and q is not None or p is not None and q is None: #structure is different
            return False      
        return p.val == q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right) #checks current,left,right  

        
        
        