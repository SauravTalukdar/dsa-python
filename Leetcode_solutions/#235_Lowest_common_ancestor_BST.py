# Problem: Lowest Common Ancestor of a Binary Search Tree
# LeetCode: #235
# Difficulty: Medium
# Time Complexity: O(H) — O(log N) for balanced trees, O(N) for skewed trees
# Space Complexity: O(H)
# Approach: Recursive DFS using BST properties to locate the split point

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#approch1. Explicitly taking small or great to find the split or if root is equal to p OR q
class Solution:
    def lowestCommonAncestor1(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        smaller = p.val if p.val < q.val else q.val
        greater = p.val if p.val > q.val else q.val
        if root is None:
            return None  
        if smaller < root.val < greater or (q.val == root.val or p.val == root.val):
            return root  
        elif p.val < root.val and q.val < root.val: 
            return self.lowestCommonAncestor1(root.left,p,q)
        elif p.val > root.val and q.val > root.val:   
            return self.lowestCommonAncestor1(root.right,p,q)
        

#approch2. Better/cleaner 
# (handling the explicit checking directly in else block as anything other than the other two conditions we return root)
    def lowestCommonAncestor2(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None   
        elif p.val < root.val and q.val < root.val: #if both p and q are smaller than root search the left
            return self.lowestCommonAncestor2(root.left,p,q)
        elif p.val > root.val and q.val > root.val:  #if both p and q are greater than root search the right        
            return self.lowestCommonAncestor2(root.right,p,q)
        else:  #if p or q < root < p or q , OR p or q == root 
            return root    