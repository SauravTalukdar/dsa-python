#Write a function to find the length of the shortest path between two nodes in a weighted graph.

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

#test case1
num_nodes1 = 6
edges1 = [(0,1,4),(0,2,2),(1,2,5),(1,3,10),(2,4,3),(3,5,11),(4,3,4)]
graph1 = Graph(num_nodes1,edges1,directed=True,weighted=True)

#test case2
num_nodes2 = 9
edges2 = [(0,1,3),(0,3,2),(0,8,4),(1,7,4),(2,7,2),(2,3,6),(2,5,1),(3,4,1),(4,8,8),(5,6,8)]
graph2 = Graph(num_nodes2,edges2,weighted=True)


#dijkstra algorithm         
def shortest_path(graph,source,target):
    visited = [False] * len(graph.data)
    parent = [None] * len(graph.data)
    distance = [float('inf')] * len(graph.data)
    queue = []

    distance[source] = 0
    queue.append(source)
    idx = 0

    while idx < len(queue) and not visited[target]:
        current = queue[idx]
        visited[current] = True
        idx += 1
        update_distances(graph,current,distance,parent)
        next_node = pick_next_node(distance,visited)
        if next_node is not None:
            queue.append(next_node)

    return distance[target],parent

def update_distances(graph,current,distance,parent=None): #update distances of the current nodes neighbours
    neighbours = graph.data[current]
    weights = graph.weight[current]
    for i,node in enumerate(neighbours):
        weight = weights[i]
        if distance[current] + weight < distance[node]:
            distance[node] = distance[current] + weight
            if parent is not None:
                parent[node] = current

def pick_next_node(distance,visited): #pick the next unvisited node at the smallest distance
    min_distance = float('inf')
    min_node = None
    for node in range(len(distance)):
        if not visited[node] and distance[node] < min_distance:
            min_node = node
            min_distance = distance[node]
    return min_node

print(shortest_path(graph1,0,5))
print(shortest_path(graph2,0,7))

     

