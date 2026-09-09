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
        elif key < root.val: 
            root.left = self.deleteNode(root.left,key) #recursively run delete on left subtree
        elif key > root.val:
            root.right = self.deleteNode(root.right,key) #recursively run delete on right subtree
        else:
            if root.left is None: #if root doesnt have left subtree
                return root.right #make the right its replacement
            elif root.right is None: #if right is not there
                return root.left #make the left its replacement
           
            succesor = self.find_min(root.right) #find the inorder succesor(smallest element in right subtree)
            root.val = succesor.val #replace targets value with the sucessors value
            root.right = self.deleteNode(root.right,succesor.val) #delete the original succesor,after replacement
        return root #return the root for output and recursion call

    def find_min(self,node): #minimum element is always the leftmost element
        while node.left is not None: #keep going left until u cant anymore
            node = node.left #constantly assigning node's left to make it the node
        return node #return the end node(min) 

#the inorder successor is used as a replacement as it is the smallest value in the right subtree
#so when it replaces the target root it is greater than everything in left subtree and smaller than the right subtree                
                