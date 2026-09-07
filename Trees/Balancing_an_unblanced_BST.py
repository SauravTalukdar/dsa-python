#balancing an unbalanced BST
#first we perform an inorder traversal to make a sorted list
#then we create a balanced BST with the earlier function(balanced_bst)

class BSTNode:
    def __init__(self,key,value = None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent= None

class User: #created a user class to store of users (input)
    def __init__(self,username,name,email):
        self.username = username
        self.name = name
        self.email = email

    def __repr__(self):
        return f"Username: {self.username}, name: {self.name}, email: {self.email}"

    def __str__(self):
        return self.__repr__()

def insert(node,key,value):
    if node is None:
        node = BSTNode(key,value)
    elif key < node.key:
        node.left = insert(node.left,key,value)
        node.left.parent = node
    elif key > node.key:
        node.right = insert(node.right,key,value)
        node.right.parent = node
    return node

users = [
    ('aakash' ,User(username = 'aakash',name = 'Aakash Rai',email =  'aakash@example.com')),
    ('bibek',User(username ="bibek",name ="bibekroy",email = "bibek@gmail")),            
    ('biraj',User(username ='biraj', name ='Biraj Das', email = 'biraj@example.com')),
    ('hemanth',User(username ='hemanth', name ='Hemanth Jain', email = 'hemanth@example.com')),
    ('jadhesh',User(username ='jadhesh',name = 'Jadhesh Verma',email =  'jadhesh@example.com')),
    ('raktim',User(username ="raktim",name ="raktimborah",email = "raktim@gmail")),
    ('saurav',User(username ="saurav",name ="sauravtalukdar",email = "saurav@gmail")),      
    ('sonaksh',User(username ='sonaksh',name = 'Sonaksh Kumar',email =  'sonaksh@example.com')),
    ('vishal',User(username ='vishal',name = 'Vishal Goel', email = 'vishal@example.com')),
    ('tanushka',User(username ="tanushka",name ="tanushkaroy",email = "tanushka@gmail"))]          

def display_keys(node,space='\t',level=0):
    if node is None:
        print(space*level + 'Ø')
        return
    if node.left is None and node.right is None:
        print(space*level + str(node.key))
        return
    display_keys(node.right,space,level+1)
    print(space*level + str(node.key))
    display_keys(node.left,space,level+1)

def balanced_bst(data,low = 0,high = None,parent = None):
    if high is None:
        high = len(data) - 1 #set high to the length of the list
    if low > high:
        return None #if we traverse through all elements return None(no elements left)
    mid = (low + high) // 2
    key,value = data[mid] #store mid of the list
    root = BSTNode(key,value) #create root node with mid
    root.parent = parent #set the parent
    root.left = balanced_bst(data,low,mid - 1,root)  #also pass the root as the parent for the left tree     
    root.right = balanced_bst(data,mid + 1,high,root) #also pass the root as the parent for the right tree
    return root 

#creating the sorted list(by inorder traversal)
def list_all(node):
    if node is None:
        return []
    return list_all(node.left) + [(node.key,node.value)] + list_all(node.right) #had to wrap the node.key,node.value in a tuple   

#function to balance create the balanced BST
def balance_bst(node):
    return balanced_bst(list_all(node))

tree1 = None #creating empty tree

for username , user in users: #inserting values in the tree
    tree1 = insert(tree1,username,user)

display_keys(tree1) #unbalanced tree

tree2 = balance_bst(tree1) #balancing the unbalanced tree

display_keys(tree2) #balanced tree