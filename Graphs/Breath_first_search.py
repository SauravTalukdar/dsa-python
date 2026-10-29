num_nodes = 5
edges = [(0,1),(0,4),(1,2),(1,3),(1,4),(2,3),(3,4)]

class Graph:
    def __init__(self,num_nodes,edges):
        self.num_nodes = num_nodes
        self.data = [[] for _ in range(num_nodes)] 
        for n1,n2 in edges:
                self.data[n1].append(n2)
                self.data[n2].append(n1)

    def add_edge(self,n1,n2):
        if n1 < self.num_nodes and n2 < self.num_nodes:
            if n2 not in self.data[n1]: 
                self.data[n1].append(n2)
                self.data[n2].append(n1)

    def remove_edge(self,n1,n2):
        if n1 < self.num_nodes and n2 < self.num_nodes:
            if n2 in self.data[n1]:
                self.data[n1].remove(n2)          
                self.data[n2].remove(n1)          

    def __repr__(self):
        return "\n".join(["{}:{}".format(n, neighbours) for n,neighbours in enumerate(self.data)]) 
    def __str__(self):
        return self.__repr__()                        

graph1 = Graph(num_nodes,edges)

#implementing bfs
def bfs(graph,root):
    queue = [] #nodes to process, visited but neighbours not yet checked
    discovered = [False] * len(graph.data) #tracks which nodes have been seen, prevents revisiting
    distance = [None] * len(graph.data) #how many edges from root to each node
    parent = [None] * len(graph.data) #which node led to each node (useful for finding paths)
    #All indexed by node number. For 5 nodes — each list has 5 elements.

    discovered[root] = True #start from root mark it discovered
    queue.append(root) #add root to queue
    distance[root] = 0 #distance of root to itself is 0
    idx = 0 #this tracks current position in queue

    while idx < len(queue): #processes nodes one by one till its empty
        #dequeue
        current = queue[idx] #current node being processed
        idx += 1 #advance to next node

        #check all edges of current(means check its neighbours)
        for node in graph.data[current]: 
            if not discovered[node]: #if not discovered do all these
                distance[node] = 1 + distance[current] #distance is plus one
                parent[node] = current #parent is the current node
                discovered[node] = True #mark as discovered
                queue.append(node) #add to the queue

    return queue,distance,parent     

#checking if all the nodes in the graph are connected
def is_connected(graph):
    queue, distance, parent = bfs(graph, 0) #run bfs from node 0
    # if any node has distance None — it was never reached by BFS
    # meaning it's in a separate disconnected component
    # if no None in distance — all nodes were reached — graph is connected
    return None not in distance #gives false if none in distance(otherwise checks if none is in distance->returns true)

#full trace    
# Graph edges: [(0,1),(0,4),(1,2),(1,3),(1,4),(2,3),(3,4)]

# Node 3’s neighbours: [1, 2, 4]
# Node 1’s neighbours: [0, 2, 3, 4] etc.

# Start: queue=[3], discovered[3]=True, distance[3]=0

# idx=0, current=3
#     neighbours of 3: [1, 2, 4]
#     1 not discovered → distance[1]=1, parent[1]=3, queue=[3,1]
#     2 not discovered → distance[2]=1, parent[2]=3, queue=[3,1,2]
#     4 not discovered → distance[4]=1, parent[4]=3, queue=[3,1,2,4]

# idx=1, current=1
#     neighbours of 1: [0, 2, 3, 4]
#     0 not discovered → distance[0]=2, parent[0]=1, queue=[3,1,2,4,0]
#     2 already discovered → skip
#     3 already discovered → skip
#     4 already discovered → skip

# idx=2, current=2
#     neighbours of 2: [1, 3]
#     1 already discovered → skip
#     3 already discovered → skip

# idx=3, current=4
#     neighbours of 4: [0, 1, 3]
#     0 already discovered → skip
#     1 already discovered → skip
#     3 already discovered → skip

# idx=4, current=0
#     neighbours of 0: [1, 4]
#     1 already discovered → skip
#     4 already discovered → skip

# idx=5 = len(queue) → loop ends

print(bfs(graph1,3))
print(is_connected(graph1))

