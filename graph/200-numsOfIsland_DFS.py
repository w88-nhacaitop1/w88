""" 200. Number of Islands
https://leetcode.com/problems/number-of-islands/

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

* Input:
*    11110
*    11010
*    11000
*    00000
* Output: 1

* Input:
*    11000
*    11000
*    00100
*    00011
* Output: 3 """

# TODO: Approach 1: DFS - Depth First Search (Accepted)         [O(M x N) & O(M x N)]
# https://www.geeksforgeeks.org/find-number-of-islands/
# TODO: Approach 2: BFS - Breath First Search (Accepted)        [O(M x N) & O(min(M,N))]
# TODO: Approach 3: Union Find (aka Disjoin Set) (Accepted)     [O(M x N) & O(M x N)]


class Graph:
    def __init__(self, row, col, g):
        self.ROW = row
        self.COL = col
        self.graph = g

    # A function to check if a given cell
    # (row, col) can be included in DFS
    def isSafe(self, i, j, visited):
        # row number is in range, column number
        # is in range and value is 1
        # and not yet visited
        return (i >= 0 and i < self.ROW and
                j >= 0 and j < self.COL and
                not visited[i][j] and self.graph[i][j])

    # A utility function to do DFS for a 2D
    # boolean matrix. It only considers
    # the 8 neighbours as adjacent vertices
    def DFS(self, i, j, visited):
        rowNbr = [-1, -1, -1,  0, 0,  1, 1, 1]
        colNbr = [-1,  0,  1, -1, 1, -1, 0, 1]

        # Mark this cell as visited
        visited[i][j] = True

        # Recur for all connected neighbours
        for k in range(8):
            if self.isSafe(i + rowNbr[k], j + colNbr[k], visited):
                self.DFS(i + rowNbr[k], j + colNbr[k], visited)

    # The main function that returns
    # count of islands in a given boolean
    # 2D matrix
    def countIslands(self):
        # Make a bool array to mark visited cells.
        # Initially all cells are unvisited
        visited = [[False for j in range(self.COL)] for i in range(self.ROW)]

        # Initialize count as 0 and travese
        # through the all cells of
        # given matrix
        count = 0
        for i in range(self.ROW):
            for j in range(self.COL):
                # If a cell with value 1 is not visited yet,
                # then new island found
                if visited[i][j] == False and self.graph[i][j] == 1:
                    # Visit all cells in this island
                    # and increment island count
                    self.DFS(i, j, visited)
                    count += 1

        return count


if __name__ == "__main__":
    # graph = [[1, 1, 0, 0, 0],
    #          [0, 1, 0, 0, 1],
    #          [1, 0, 0, 1, 1],
    #          [0, 0, 0, 0, 0],
    #          [1, 0, 1, 0, 1]]

    graph = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]

    row = len(graph)
    col = len(graph[0])

    g = Graph(row, col, graph)

    print("Number of islands is: ", end="")
    print(g.countIslands())

    # This code is contributed by Neelam Yadav
