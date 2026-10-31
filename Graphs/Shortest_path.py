#Write a function to find the length of the shortest path between two nodes in a weighted graph.

# Dijkstra's Shortest Path (simple version)
# Time Complexity: O(V^2) - pick_next_node scans all nodes each round
# Space Complexity: O(V) - visited, parent, distance, queue
# Approach: lock in the closest unvisited node, then relax its neighbours' distances
# Limitation: does not work with negative edge weights

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
    visited = [False] * len(graph.data) #One True/False slot per node. True means this node’s shortest distance is final and we’re done with it.
    parent = [None] * len(graph.data) #parent[x] is the node we came from to reach x on the best path. It lets you rebuild the path later.
    distance = [float('inf')] * len(graph.data) #The best known distance to each node. Everything starts at infinity because we haven’t found any route yet.
    queue = [] #The order in which nodes get processed.

    distance[source] = 0 #Getting to the source is 0. 
    queue.append(source) # We put it in the queue
    idx = 0 #and set idx = 0 so we start at the first item.

    while idx < len(queue) and not visited[target]: #Keep going while:there are still nodes in the queue to process, and
                                                    # the target hasn’t been locked in yet.
                                                    #Once the target is visited, its distance is final, so we can stop early.
        current = queue[idx] #take the next node
        visited[current] = True #lock it in
        idx += 1 #move index forward
        update_distances(graph,current,distance,parent) #Look at all of current’s neighbours and see if we found shorter routes to them.
        next_node = pick_next_node(distance,visited) #Choose the closest unvisited node 
        if next_node is not None: #If nothing is left (None), add nothing, and the loop ends naturally.
            queue.append(next_node) #add it to the queue so the next round processes it.

    return distance[target],parent #Return the shortest distance to the target, plus the parent list.

def update_distances(graph,current,distance,parent=None): #update distances of the current nodes neighbours
    neighbours = graph.data[current] #neighbours is the list of nodes current connects to.
    weights = graph.weight[current] #weights is the list of edge costs, in the same order.
    for i,node in enumerate(neighbours): #Go through each neighbour. i is the position, node is the neighbour
        weight = weights[i] #weights[i] is the cost of that edge.
        if distance[current] + weight < distance[node]: #distance[current] + weight is the cost of reaching node through current. 
                                                        #If that’s cheaper than the best distance we already know, we’ve found a shorter route.
            distance[node] = distance[current] + weight #Update the best distance
            if parent is not None: 
                parent[node] = current

def pick_next_node(distance,visited): #pick the next unvisited node at the smallest distance
    min_distance = float('inf') #Start with “nothing found yet”.
    min_node = None
    for node in range(len(distance)): #Scan all nodes.
        if not visited[node] and distance[node] < min_distance: #Among the unvisited ones, if distance is also less than min distance
            min_node = node #store the node
            min_distance = distance[node] #store the distance of the node
    return min_node #return it
    #If every unvisited node is still at infinity (unreachable), None comes back.

print(shortest_path(graph1,0,5))
print(shortest_path(graph2,0,7))

# A small trace

# Edges (directed): 0→1 (cost 4), 0→2 (cost 2), 2→1 (cost 1), 1→3 (cost 5). Source is 0, target is 3.

# distance = [0, inf, inf, inf]      visited = [F, F, F, F]

# Round 1

# shortest_path sets current = 0 and visited[0] = True.
# update_distances looks at node 0’s neighbours:
# Node 1: 0 + 4 = 4, better than inf, so distance[1] = 4.
# Node 2: 0 + 2 = 2, better than inf, so distance[2] = 2.
# pick_next_node checks the unvisited nodes: 1 (4), 2 (2), 3 (inf). It returns 2.
# distance = [0, 4, 2, inf]

# Round 2

# current = 2, visited[2] = True.
# update_distances looks at node 2’s neighbours:
# Node 1: 2 + 1 = 3, which is better than 4, so distance[1] = 3 and parent[1] = 2.
# pick_next_node checks 1 (3) and 3 (inf). It returns 1.
# distance = [0, 3, 2, inf]

# The route to node 1 improved from 4 to 3. That is the core of the algorithm.

# Round 3

# current = 1, visited[1] = True.
# update_distances looks at node 1’s neighbours:
# Node 3: 3 + 5 = 8, so distance[3] = 8 and parent[3] = 1.
# pick_next_node returns 3.
# distance = [0, 3, 2, 8]

# Round 4

# current = 3, visited[3] = True.
# The target is now visited, so the while condition fails and the loop stops.

# Answer: distance[3] = 8.

# parent = [None, 2, 0, 1]
# Path: 3 ← 1 ← 2 ← 0, which is 0 → 2 → 1 → 3