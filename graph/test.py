import math
import numbers

def numCells(grid):
    # Write your code here
    count = 0
    for row in range(len(grid)):
        for col in range(len(grid)):
            isDominantCell(row, col, grid)
        
def isDominantCell(row: int, col:int, grid):
    rowNbrs = [-1, -1, -1,  0, 0,  1, 1, 1]
    colNbrs = [-1,  0,  1, -1, 1, -1, 0, 1]

    maxValue = grid[row, col]
    
    for k in range(8):
        i = row + rowNbrs[k]
        j = col + colNbrs[k]
        
        if isSafe(i, j, grid):
            maxValue = math.max(grid[i, j], maxValue)
        
    return maxValue == grid[row,col]

def isSafe(i, j, grid):
    return (i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0]))


if __name__ == '__main__':
     grid = [[1, 2, 7], [4, 5, 6], [8, 8, 9]]

     numCells(grid)