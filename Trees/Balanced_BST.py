#creating a Balanced BST from a sorted list/array

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

#function to create the balanced BST   
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

#creating a list of users with key and value pairs in sorted order
users = [
    ('aakash' ,User(username = 'aakash',name = 'Aakash Rai',email =  'aakash@example.com')),
    ('bibek',User(username ="bibek",name ="bibekroy",email = "bibek@gmail")),            
    ('biraj',User(username ='biraj', name ='Biraj Das', email = 'biraj@example.com')),
    ('hemanth',User(username ='hemanth', name ='Hemanth Jain', email = 'hemanth@example.com')),
    ('jadhesh',User(username ='jadhesh',name = 'Jadhesh Verma',email =  'jadhesh@example.com')),
    ('raktim',User(username ="raktim",name ="raktimborah",email = "raktim@gmail")),
    ('saurav',User(username ="saurav",name ="sauravtalukdar",email = "saurav@gmail")),      
    ('sonaksh',User(username ='sonaksh',name = 'Sonaksh Kumar',email =  'sonaksh@example.com')),
    ('tanushka',User(username ="tanushka",name ="tanushkaroy",email = "tanushka@gmail")),            
    ('vishal',User(username ='vishal',name = 'Vishal Goel', email = 'vishal@example.com'))]

#creating the balanced tree
tree = balanced_bst(users)

#displaying the tree
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

display_keys(tree)