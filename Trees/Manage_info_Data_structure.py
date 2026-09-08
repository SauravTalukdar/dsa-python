#full implementation of a management of profiles database 
class TreeMap:
    def __init__(self):
        self.root = None #creating a tree

    def __setitem__(self,key,value):
        node = find(self.root,key) #finding a node
        if not node: #if not found inserting a node
            self.root = insert(self.root,key,value)
            self.root = balance_bst(self.root) #balancing after every insertion
        else:
            update(self.root,key,value) #if found updating value

    def __getitem__(self,key):
        node = find(self.root,key)
        return node.value if node else None #getting value of a node

    def __iter__(self):
        return (x for x in list_all(self.root)) #creating a generic function to store all nodes

    def __len__(self): #length of the tree
        return size(self.root)

    def display(self): #displaying the tree
        return display_keys(self.root)

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

def size(node):
    if node is None:
        return 0
    return 1 + size(node.left) + size(node.right) 

def update(node,key,value):
    target = find(node,key)
    if target is not None:
        target.value = value

def find(node,key):
    if node is None:
        return None
    if key == node.key:
        return node
    elif key < node.key:
        return find(node.left,key)
    elif key > node.key:
        return find(node.right,key)

def balance_bst(node):
    return balanced_bst(list_all(node))

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

def list_all(node):
    if node is None:
        return []
    return list_all(node.left) + [(node.key,node.value)] + list_all(node.right) #had to wrap the node.key,node.value in a tuple    

users = [User(username='aakash', name='Aakash Rai', email='aakash@example.com'),
User(username='biraj', name='Biraj Das', email='biraj@example.com'),
User(username='hemanth', name='Hemanth Jain', email='hemanth@example.com'),
User(username='jadhesh', name='Jadhesh Verma', email='jadhesh@example.com'),
User(username='siddhant', name='Siddhant U', email='siddhantu@example.com'),
User(username='sonaksh', name='Sonaksh Kumar', email='sonaksh@example.com'),
User(username='vishal', name='Vishal Goel', email='vishal@example.com')]

treemap = TreeMap() #creating the object

#inserting the nodes or setting them
#not so convinient
# treemap.__setitem__('aakash',users[0]) 
# treemap.__setitem__('jadhesh',users[3])
# treemap.__setitem__('sonaksh',users[5])

#convinient
treemap['aakash'] = users[0]
treemap['jadhesh'] = users[3]
treemap['sonaksh'] = users[5]
treemap['bibek'] = users[1]

#getting a user info
print(treemap['bibek'])

#lenght(size) of the tree
print(len(treemap))

treemap.display()



