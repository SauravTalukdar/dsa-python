class Treenode: #created a treenode class for nodes
    def __init__(self,key):
        self.key = key #containing key(or value or both)
        self.left = None #left pointer empty(for now)
        self.right = None #right pointer empty(for now)

#creating nodes
node0 = Treenode(3) #root node       
node1 = Treenode(4)        
node2 = Treenode(5)

node0.left = node1 #connecting node0 left to node1
node0.right = node2 #connecting node0 right to node2

