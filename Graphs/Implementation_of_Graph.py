num_nodes = 5 #number of nodes in the graph
edges = [(0,1),(0,4),(1,2),(1,3),(1,4),(2,3),(3,4)] #these represent edges(connections) between the nodes
#by these two information we can draw the graphg= in a peace of paper(but this is not the most efficient)

#Q) Create a class to represent a graph as an adjacency list 
#Adjacency list - Each node stores a list of its direct neighbours

class Graph:
    def __init__(self,num_nodes,edges):
        self.num_nodes = num_nodes #store total number of nodes
        self.data = [[] for _ in range(num_nodes)] #Create an adjacency list — one empty list per node. 
                                                 #Index represents the node, list contains its neighbours.
                                                 #self.data = [[], [], [], [], []]
                                                 #index:       0   1   2   3   4
        for n1,n2 in edges: #For each edge — add both directions. 
                self.data[n1].append(n2) #Graph is undirected so if node 1 connects to node 3 
                self.data[n2].append(n1)#node 3 also connects to node 1.

    def add_edge(self,n1,n2): #adding an edge
        if n1 < self.num_nodes and n2 < self.num_nodes: #checking if the nodes n1 and n2 are valid
            if n2 not in self.data[n1]: #checking duplicate(we can just check one node as the graph is undirected)
                self.data[n1].append(n2)
                self.data[n2].append(n1)

    def remove_edge(self,n1,n2):
        if n1 < self.num_nodes and n2 < self.num_nodes:
            if n2 in self.data[n1]: #check if the edge exists(as we need to remove it)
                self.data[n1].remove(n2)          
                self.data[n2].remove(n1)          

    def __repr__(self):
        return "\n".join(["{}:{}".format(n, neighbours) for n,neighbours in enumerate(self.data)]) #represent each node with its neighbours
    def __str__(self):
        return self.__repr__()                

graph1 = Graph(num_nodes,edges)
print(graph1)



  