class TreeNode:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None

class Solution:
    def traverse_in_order(self,node):
        if node is None: #if node/subtree is empty return an empty list
            return []
        return (self.traverse_in_order(node.left) + [node.key] + self.traverse_in_order(node.right))
                

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
traversal = Solution()
print(traversal.traverse_in_order(tree))


