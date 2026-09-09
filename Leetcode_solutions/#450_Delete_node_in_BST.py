# Problem: Delete Node in a BST
# LeetCode: #450
# Difficulty: Medium
# Time Complexity: O(h) — h is height of tree
# Space Complexity: O(h) — recursion call stack
# Approach: Recursive — find and delete in one pass, no parent pointer needed
# Case 1: Leaf or one child — return the existing child (or None)
# Case 2: Two children — replace with inorder successor, delete successor recursively

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        if key < root.val:
            root.left = self.deleteNode(root.left,key)   
        elif key > root.val:
            root.right = self.deleteNode(root.right,key)
        else:
            if root.left is None:
                return root.right 
            elif root.right is None:
                return root.left
            successor = self.find_min(root.right)
            root.val = successor.val
            root.right = self.deleteNode(root.right, successor.val)  
        return root 

    
    def find_min(self, node):
        while node.left is not None:
            node = node.left
        return node                   
                