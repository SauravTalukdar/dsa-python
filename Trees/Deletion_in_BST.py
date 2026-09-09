class BSTNode:
    def __init__(self,key,value=0):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

class User: #created a user class to store of users (input)
    def __init__(self,username,name,email):
        self.username = username
        self.name = name
        self.email = email

    def __repr__(self):
        return f"Username: {self.username}, name: {self.name}, email: {self.email}"

    def __str__(self):
        return self.__repr__()        

aakash = User('aakash', 'Aakash Rai', 'aakash@example.com')
biraj = User('biraj', 'Biraj Das', 'biraj@example.com')
hemanth = User('hemanth', 'Hemanth Jain', 'hemanth@example.com')
jadhesh = User('jadhesh', 'Jadhesh Verma', 'jadhesh@example.com')
sonaksh = User('sonaksh', 'Sonaksh Kumar', 'sonaksh@example.com')
vishal = User('vishal', 'Vishal Goel', 'vishal@example.com')
saurav = User("saurav","sauravtalukdar","saurav@gmail")            
tanushka = User("tanushka","tanushkaroy","tanushka@gmail")            
bibek = User("bibek","bibekroy","bibek@gmail")            
raktim = User("raktim","raktimborah","raktim@gmail")  

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

tree1 = insert(None,jadhesh.username,jadhesh)
insert(tree1,biraj.username,biraj)                
insert(tree1,sonaksh.username,sonaksh)                
insert(tree1,aakash.username,aakash)                
insert(tree1,hemanth.username,hemanth)                
insert(tree1,saurav.username,saurav)                
insert(tree1,tanushka.username,tanushka)

def find(node,key):
    if node is None:
        return None
    if key == node.key:
        return node
    elif key < node.key:
        return find(node.left,key)
    elif key > node.key:
        return find(node.right,key) 

#function to delete a node
def delete(node,key):
    target = find(node,key) #finding the ttarget
    if target.left is None and target.right is None: #this is a leaf node 
        if target.parent.left == target: 
            target.parent.left = None  #we set parents pointer to None in this case
        else:
            target.parent.right = None    
    elif target.left is None or target.right is None: #this is a node with one child
        child = target.left if target.left is not None else target.right #we see which child is not missing
        if target.parent.left == target: 
            target.parent.left = child #directly connect parent to the targets child
        else:
            target.parent.right = child
        if child is not None:
            child.parent = target.parent    
    elif target.left is not None and target.right is not None: #node with two children
        succesor = find_min(target.right)
        # replace the targets key and value with the inorder succesors key and Value
        target.key = succesor.key
        target.value = succesor.value
        #connect the nodes
        if succesor.parent.left == succesor: 
            succesor.parent.left = succesor.right
        else:
            succesor.parent.right = succesor.right 

        if succesor.right is not None:
            succesor.right.parent = succesor.parent

def find_min(node): #helper function to find inorder succesor
        while node.left is not None:
            node = node.left
        return node 

#1.Delete leaf node
delete(tree1,'saurav')
#2. Delete node with two childer
delete(tree1,'sonaksh')

display_keys(tree1)


    


    

