#to check if a Binary tree is balanced we check ->
#1.Ensure the left subtree is balanced
#2.Ensure the right subtree is balanced
#3.Ensure the difference in height of left and right subtree is not more than 1,i.e, <=1

def is_balanced(node):
    if node is None:
        return True, 0 #returning True if no nodes and height 0
    balanced_l, height_l = is_balanced(node.left) #checking for left    
    balanced_r, height_r = is_balanced(node.right)#checking for right
    balanced = balanced_l and balanced_r and abs(height_l - height_r) <= 1 #checking if tree is balanced with the conditions
    height = 1 + max(height_l,height_r)#calculating max height
    return balanced,height#returning to the function for recursive call and also output  