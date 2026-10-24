#implementing directed and weighted graphs using a class

class Graph:
    def __init__(self,num_nodes,edges,directed = False,weighted = False):
        self.num_nodes = num_nodes
        self.directed = directed
        self.weighted = weighted
        self.data = [[] for _ in range(num_nodes)] #store the adjacency list
        self.weight = [[] for _ in range(num_nodes)] #store the weights of the edges
        for edge in edges:
            if self.weighted: #if it has a weight
                n1,n2,weight = edge #unpack the two edges and the weight
                self.data[n1].append(n2) #connect one edge
                self.weight[n1].append(weight) #add the weight to n1's weight
                if not directed:
                    self.data[n2].append(n1) #connect the other edge
                    self.weight[n2].append(weight) #add the weight of the other edge
            else: #if it doesnt have a weight
                n1,n2 = edge #unpack only the edges(no weight)
                self.data[n1].append(n2) #add first edge
                if not directed:
                    self.data[n2].append(n1)  #add the 2nd edge
    def __repr__(self):
        result = ""
        for n, neighbours in enumerate(self.data):
            if self.weighted:
                # show each neighbour with its weight
                pairs = [f"{neighbour}(w={self.weight[n][i]})" 
                        for i, neighbour in enumerate(neighbours)]
                result += f"{n}: {pairs}\n"
            else:
                result += f"{n}: {neighbours}\n"
        return result

    def __str__(self):
        return self.__repr__()  

#undirected graph        
num_nodes1 = 5 
edges1 = [(0,1),(0,4),(1,2),(1,3),(1,4),(2,3),(3,4)] 

#weighted graph
num_nodes2 = 9
edges2 = [(0,1,3),(0,3,2),(0,8,4),(1,7,4),(2,7,2),(2,3,6),(2,5,1),(3,4,1),(4,8,8),(5,6,8)]

#directed graph
num_nodes3 = 5
edges3 = [(0,1),(1,2),(2,3),(2,4),(4,2),(3,0)]

graph1 = Graph(num_nodes1,edges1)
graph2 = Graph(num_nodes2,edges2,weighted=True)
graph3 = Graph(num_nodes3,edges3,directed=True)

print(graph1)
print(graph2)
print(graph3)
                      
