def balanced_bst(data,low = 0,high = None,parent = None):
    if high is None:
        high = len(data) - 1
    if lo > high:
        return None
    mid = (low + high) // 2
    key,value = data[mid]
    root = BSTNode(key,value)
    root.parent = parent
    root.left = balanced_bst(data,low,mid - 1,parent)        
    root.right = balanced_bst(data,mid + 1,high,parent)
    return root        