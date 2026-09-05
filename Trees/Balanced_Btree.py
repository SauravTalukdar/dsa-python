#to check if a Binary tree is balanced we check ->
#1.Ensure the left subtree is balanced
#2.Ensure the right subtree is balanced
#3.Ensure the difference in height of left and right subtree is not more than 1,i.e, <=1(condition for balance)

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

#function to check
#Approch 1
def is_balanced(node):
    if node is None:
        return True, 0 #returning True if no nodes and height 0
    balanced_l, height_l = is_balanced(node.left) #checking for left    
    balanced_r, height_r = is_balanced(node.right)#checking for right
    balanced = balanced_l and balanced_r and abs(height_l - height_r) <= 1 #checking if tree is balanced with the conditions
    height = 1 + max(height_l,height_r)#calculating max height
    return balanced,height#returning to the function for recursive call and also output 

#Approch 2
class Solution:
    def isBalanced(self, root):
        def height(node):
            if node is None:
                return 0
            left = height(node.left)          
            right = height(node.right)

            if left == -1 or right == -1: #checks if left or right is not balanced
                return -1  
            if abs(left - right) > 1: #checks current node
                return -1
            return 1 + max(left,right) #return current height

        return height(root) != -1 #this line gives true or false                    

#test cases
#1.unbalanced
tree1 = insert(None,aakash.username,aakash)
insert(tree1,biraj.username,biraj)                
insert(tree1,hemanth.username,hemanth)                
insert(tree1,saurav.username,saurav)                
insert(tree1,sonaksh.username,sonaksh)                                
insert(tree1,tanushka.username,tanushka)

#2.balanced
tree2 = insert(None,jadhesh.username,jadhesh)
insert(tree2,biraj.username,biraj)                
insert(tree2,sonaksh.username,sonaksh)                
insert(tree2,aakash.username,aakash)                
insert(tree2,hemanth.username,hemanth)                
insert(tree2,saurav.username,saurav)                
insert(tree2,tanushka.username,tanushka)

#3.
tree3 = insert(None,jadhesh.username,jadhesh)
insert(tree3,biraj.username,biraj)                
insert(tree3,sonaksh.username,sonaksh)                
insert(tree3,aakash.username,aakash)                
insert(tree3,hemanth.username,hemanth)                
insert(tree3,saurav.username,saurav)
insert(tree3,vishal.username,vishal)
insert(tree3,tanushka.username,tanushka)


#output
print(is_balanced(tree1))
print(is_balanced(tree2))
print(is_balanced(tree3))