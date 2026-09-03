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

#manual insertion
tree = BSTNode(jadhesh.username,jadhesh)
tree.left = BSTNode(bibek.username,bibek)  
tree.right = BSTNode(saurav.username,saurav)  


#creating a function to insert
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

display_keys(tree1)