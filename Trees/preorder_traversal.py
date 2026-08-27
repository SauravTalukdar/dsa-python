class TreeNode:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None

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

#implementing preorder traversal(root ->left-> right)
def traverse_pre_order(node):
    if node is None:
        return []
    return ([node.key] + traverse_pre_order(node.left) + traverse_pre_order(node.right))

print(traverse_pre_order(tree))                