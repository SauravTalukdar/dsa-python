# Problem: Flood Fill
# LeetCode: #733
# Difficulty: Easy
# Time: O(m*n) | Space: O(m*n) queue
# Approach: BFS from (sr, sc)
# Edge case: new color == old color → return immediately

'''
A image of a grid is given of m x n integer size. Where image[i][j] represents the pixel value of the image.
We are also given three integers sr,sc and color. Our task is to perform a flood fill from the pixel image[sr][sc]
To perform a flood fill-
1. begin with the starting pixel(image[sr][sc]) and change its color to color, i,e change its number to another given number
2. we perform the same operation of changing colors for its direct neighbours(up,down,left,right),
and the pixels that share the same color(number).
3. we keep doing this process for the neighbours of the neighbour pixels if they have the same color(number)
4. we stop when there are no more neighbouring pixels of the original color to update,i,e, all are updated to the new color(number)
'''

#input and output(example test cases)
image0 = [[1,1,1],[1,1,0],[1,0,1]]
sr0 = 1
sc0 = 1 
color0 = 2
output0 = [[2,2,2],[2,2,0],[2,0,1]]

image1 = [[0,0,0],[0,0,0]]
sr1 = 0
sc1 = 0 
color1 = 0
output1 =  [[0,0,0],[0,0,0]]

image2 = [[0,1,0],[1,1,1],[0,1,0]]
sr2 = 0
sc2 = 1
color2 = 3
output2 =  [[0,3,0],[3,3,3],[0,3,0]]

image3 = [[1]]
sr3 = 0
sc3 = 0
color3 = 5
output3 = [[5]]

image4 = [[2,2],[2,2]]
sr4 = 1
sc4 = 1
color4 = 9
output4 = [[9,9],[9,9]]

#solution
def flood_fill(image,sr,sc,color):
    old_color = image[sr][sc] #Save the colour of the starting pixel before changing anything. This is the colour we’re replacing.
    if old_color == color: #If the new colour equals the old one, nothing changes
        return image #We return early because the recolour is also our visited marker, 
        #and without this check the same cells could be added to the queue again and again.
    #grid size    
    rows = len(image) #number of rows
    cols = len(image[0]) #number of columns

    queue = [(sr,sc)] #start bfs from start cell 
    image[sr][sc] = color #recolor it imediately(which is like discovered)
    idx = 0 #pointer(same as we did in bfs)

    while idx < len(queue):
        r,c = queue[idx] #take the next cell and unpack it into row and column(its like the current)
        idx += 1 

        for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]: #Visit the four neighbours: down, up, right, left(this is the change)
            nr,nc = r + dr, c + dc #nr, nc is the neighbour’s position.
            #(we add the step to our current position to get the neighbour’s position, because (dr, dc) is only a change, not a location)
            if 0 <= nr < rows and 0 <= nc < cols and image[nr][nc] == old_color: #bound check to see - 1.neighbour inside grid(row),
                #2.neighbour inside grid(column),3.It still has the old colour, meaning it’s part of the region and hasn’t been recoloured yet
                image[nr][nc] = color #then change the color(if all conditions hold true) marking it discovered
                queue.append((nr,nc)) #add it to the queue, so that its neighbours get checked later 
    return image #return the updated image

# print(flood_fill(image0,sr0,sc0,color0))                 
# print(flood_fill(image1,sr1,sc1,color1))                 
# print(flood_fill(image2,sr2,sc2,color2))                 
# print(flood_fill(image3,sr3,sc3,color3))                 
# print(flood_fill(image4,sr4,sc4,color4))      

#Leetcode version
class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        old_color = image[sr][sc]
        if old_color == color:
            return image
        rows = len(image)    
        columns = len(image[0])

        queue = [(sr,sc)]
        image[sr][sc] = color
        idx = 0

        while idx < len(queue):
            r,c = queue[idx]
            idx +=1

            for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr,nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < columns and image[nr][nc] == old_color:
                    image[nr][nc] = color
                    queue.append((nr,nc))
        return image     

solution = Solution()
print(solution.floodFill(image0,sr0,sc0,color0))
        



