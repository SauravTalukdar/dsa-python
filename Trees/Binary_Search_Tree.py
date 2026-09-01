class TreeNode:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None

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

tree_tuple = ((4,2,5),1,3)

tree = parse_tuple(tree_tuple)

def remove_none(nums):
    return [x for x in nums if x is not None]

def is_bst(node):
    if node is None:
        return True,None,None
    is_bst_l ,min_l,max_l = is_bst(node.left)        
    is_bst_r ,min_r,max_r = is_bst(node.right)

    is_bst_node = (is_bst_l and is_bst_r and (max_l is None or node.key > max_l) and (min_r is None or node.key < min_r))
    min_key = min(remove_none([min_l, node.key, min_r]))
    max_key = max(remove_none([max_l, node.key, max_r]))
    return is_bst_node,min_key,max_key

print(is_bst(tree))       



    
