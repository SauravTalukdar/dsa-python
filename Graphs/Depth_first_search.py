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

#implementing dfs
def dfs(graph,root):
    stack = [] #nodes to process next
    discovered = [False] * len(graph.data) #tracks visited nodes
    result = [] #stores dfs traversal order
    parent = [None] * len(graph.data)

    stack.append(root) #Push root onto stack,mark discovered at pop time not here 

    while len(stack) > 0: #while there is element in stack
        current = stack.pop() #Pop from top of stack and store in current — 
        #always processes the most recently added node. This is what makes it go DEEP — latest neighbour gets processed first.
        if not discovered[current]: #check if already discovered or not,because a node can be added to stack multiple times before being processed
            discovered[current] = True #if not mark it discovered
            result.append(current) #add the element to the result list
            for node in graph.data[current]: #Push all undiscovered neighbours onto stack. processed in LIFO order
                if not discovered[node]:
                    parent[node] = current
                    stack.append(node) 
    return result                


print(dfs(graph1,3))

# BFS vs DFS — The Key Difference
# BFS → uses QUEUE → process oldest node first (FIFO)
# DFS → uses STACK → process newest node first (LIFO)
# This one difference makes BFS go wide and DFS go deep.