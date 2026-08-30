class TreeNode:
    def __init__(self,val):
        self.val = val
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

def size(node):
    if node is None:
        return 0
    return 1 + size(node.left) + size(node.right)

print(size(tree))

           