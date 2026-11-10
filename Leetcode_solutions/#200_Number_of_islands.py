# Problem: Number of islands
# LeetCode: #200
# Difficulty: Medium
# Time: O(m*n) | Space: O(m*n) queue
# Approach: BFS + Grid Traversal
# 1. Traverse the entire grid using nested loops.
# 2. Whenever an unvisited land cell ('1') is found,
#    increment the island count and start BFS.
# 3. Explore all four neighbouring directions.
# 4. Mark land cells as visited ('0') when adding them
#    to the queue to avoid duplicate visits.
# 5. Once BFS finishes, continue scanning the grid.
# 6. Every new unvisited '1' represents a new island,
#    since previous BFS traversals explored their connected land.
#
# Note: This implementation modifies the original grid.

'''
You are given a grid of characters, '1' for land and '0' for water. Count how many islands are there.
An island is a group of '1' cells connected up, down, left or right (not diagonally), and surrounded by water or the edge of the grid.
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
1 1 0 0 0
1 1 0 0 0      → island A (top-left block of four)
0 0 1 0 0      → island B (the single 1 in the middle)
0 0 0 1 1      → island C (the two 1s at the bottom right)
Output: 3 
'''

#test cases
grid0 = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output0 = 1

grid1 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output1 = 3

#all water
grid2 = [
  ["0","0","0","0","0"],
  ["0","0","0","0","0"],
  ["0","0","0","0","0"],
  ["0","0","0","0","0"]
]
Output2 = 0

#all land
grid3 = [
  ["1","1","1","1","1"],
  ["1","1","1","1","1"],
  ["1","1","1","1","1"],
  ["1","1","1","1","1"]
]
Output3 = 1

#single cell zero
grid4 = [
  ["0"]
]
Output4 = 0

#single cell one
grid5 = [
  ["1"]
]
Output5 = 1

#bfs solution
def num_islands_bfs(grid):
  count = 0 #number of islands
  rows = len(grid)
  cols = len(grid[0])
  directions = [(1,0),(-1,0),(0,1),(0,-1)] #fours possible directions for bfs traversal
  
  for i in range(rows): #traversing the entire grid
    for j in range(cols):
      root = grid[i][j] #Current cell acts as the starting point for a new BFS(inside the loop as it will change later)
      if root == '1': #if our root(start) is 1
        count += 1 #Increase the island count whenever we encounter an unvisited land cell during the grid scan. 
        #Since previous BFS traversals have already visited all connected land cells, this cell must belong to a new island.
        queue = [(i,j)] #add to the queue
        grid[i][j] = "0" #mark it as visited by marking it zero(we imediately mark it to prevent duplicate visits)
        idx = 0

        while idx < len(queue): 
          r,c = queue[idx]
          idx += 1
          for dr,dc in directions:
            nr,nc = r + dr , c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1": #check boundaries and ensure the neighbour is unvisited land(1)  
              grid[nr][nc] = "0" #change it to 0(visited)
              queue.append((nr,nc)) #add to the queue
                
  return count #return number of islands

#dfs solution
def num_islands_dfs(grid):
    count = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            root = grid[i][j]
            if root == "1":
                count +=1
                stack = [(i,j)] 
                grid[i][j] = "0"

                while len(stack) > 0:
                    r,c = stack.pop()
                    for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                        nr,nc = r + dr,c + dc
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                            grid[nr][nc] = "0"
                            stack.append((nr,nc))
    return count          

print(num_islands_dfs(grid0))          
print(num_islands_dfs(grid1))          
print(num_islands_dfs(grid2))          
print(num_islands_dfs(grid3))          
print(num_islands_dfs(grid4))          
print(num_islands_dfs(grid5))  

#Leetcode solution
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        count = 0
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        for i in range(rows):
            for j in range(cols):
                root = grid[i][j]
                if root == "1":
                    count +=1
                    queue = [(i,j)]
                    grid[i][j] = "0"
                    idx = 0
                    while idx < len(queue):
                        r,c = queue[idx]
                        idx +=1
                        for dr,dc in directions:
                            nr,nc = r + dr , c + dc
                            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                                grid[nr][nc] = "0"
                                queue.append((nr,nc))
        return count                    



      