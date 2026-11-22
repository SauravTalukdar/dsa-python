# Problem: Valid Sudoku
# LeetCode: #36
# Difficulty: Medium
# Approach 1: three separate checks (rows, columns, 3x3 boxes), each with a fresh set. return True only after all pass.
# Time: O(1) for the fixed 9x9 board (about 243 cell visits); O(n^2) if generalised to an n x n board

'''
We are given a 9x9 sudoku board, we need to determine if it is valid or not. 
Only the filled cells need to be validated according to these rules.
Rules - 
1. Each row must contain the digits 1-9 without repetition.
2. Each column must contain the digits 1-9 without repetition.
3. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition. 
Note:
A Sudoku board (partially filled) could be valid but is not necessarily solvable.

Input is a list of lists which is a grid of 9x9 boxes
Output is True(valid) or False(Not valid)
'''

#test cases
test0 = [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]

test1 = [["8","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]

test2 = [["5","3",".",".","7",".","3",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]

test3 = [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["5",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]

test4 = [["5","3",".",".","7",".",".",".","."]
        ,["6",".","3","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]  

test5 = [['.','.', '.', '.', '.', '.', '.', '.', '.'], 
        ['.', '.', '.', '.', '.', '.', '.', '.', '.'], 
        ['.', '.', '.', '.', '.', '.', '.', '.', '.'], 
        ['.', '.', '.', '.', '.', '.', '.', '.', '.'], 
        ['.', '.', '.', '.', '.', '.', '.', '.', '.'], 
        ['.', '.', '.', '.', '.', '.', '.', '.', '.'], 
        ['.', '.', '.', '.', '.', '.', '.', '.', '.'], 
        ['.', '.', '.', '.', '.', '.', '.', '.', '.'], 
        ['.', '.', '.', '.', '.', '.', '.', '.', '.']]

tests = [(test0, True), (test1, False), (test2, False),
         (test3, False), (test4, False), (test5, True)]

def sudoku(board):
    rows = len(board)
    cols = len(board[0])

    #checking rows
    for i in range(rows): #take each row 
        seen = set() #start a fresh set for it
        for j in range(cols): #go through 9 cells of the row
            if board[i][j] == ".": #"." means empty so skip it
                continue
            elif board[i][j] in seen: #if its already in seen , the number appears twice in the row(so it makes the board invalid)
                return False
            seen.add(board[i][j]) #if not seen previously remember the digit and move on

    #checking columns
    #This is the same code with the indexes swapped. 
    #In board[j][i], i is now the column and j is the row, so the inner loop walks down column i.
    for i in range(rows):
        seen = set()
        for j in range(cols):
            if board[j][i] == ".":
                continue 
            elif board[j][i] in seen:
                return False
            seen.add(board[j][i]) 

    #checking boxes
    for i in range(0,rows,3): #range(0, 9, 3) gives 0, 3 and 6, the top-left corners of the boxes.
        for j in range(0,cols,3): #The two loops together visit all nine corners: (0,0), (0,3), (0,6), (3,0), and so on
            seen = set() #fresh seen is created for each box
            for r in range(3): #Walk the 3 rows and 3 columns of the box
                for c in range(3):
                    cell = board[i + r][j + c] #i + r and j + c are the corner plus an offset from 0 to 2, so you reach all 9 cells
                    if cell == ".":
                        continue
                    elif cell in seen:
                        return False
                    seen.add(cell)
    return True #if all checks pass return True     
                     
for i, (board, expected) in enumerate(tests):
    print(i, "PASSED" if sudoku(board) == expected else "FAILED")


