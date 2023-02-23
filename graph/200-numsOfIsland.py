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
* Output: 3 
"""

# TODO: Approach 1: DFS - Depth First Search (Accepted)         [O(M x N) & O(M x N)]
# https://www.geeksforgeeks.org/find-number-of-islands/
# TODO: Approach 2: BFS - Breath First Search (Accepted)        [O(M x N) & O(min(M,N))]
# TODO: Approach 3: Union Find (aka Disjoin Set) (Accepted)     [O(M x N) & O(M x N)]

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    count += 1
                    # self.DFS(row, col, grid)
                    self.BFS(row, col, grid)

        print(grid)
        return count

    def DFS(self, row, col, grid):
        grid[row][col] = '2'
        # Recur all neighbors
        for next_row, next_col in [(row, col+1), (row, col-1), (row+1, col), (row-1, col)]:
            # IsSafe()
            if (0 <= next_row < len(grid) and
                0 <= next_col < len(grid[0]) and
                    grid[next_row][next_col] == '1'):
                self.DFS(next_row, next_col, grid)

    def BFS(self, row, col, grid):
        grid[row][col] = '2'  # ? Visited = 2
        queue = [(row, col)]

        while queue:
            nxt_lst = []
            for current_row, current_col in queue:
                for next_row, next_col in [(current_row, current_col+1), (current_row, current_col-1), (current_row+1, current_col), (current_row-1, current_col)]:
                    if (0 <= next_row < len(grid) and
                        0 <= next_col < len(grid[0]) and
                            grid[next_row][next_col] == '1'):
                        grid[next_row][next_col] = '2'
                        nxt_lst.append((next_row, next_col))
            queue = nxt_lst


if __name__ == "__main__":
    graph1 = [
        ['1', '1', '1', '1', '0'],
        ['1', '1', '0', '1', '0'],
        ['1', '1', '0', '0', '0'],
        ['0', '0', '0', '0', '0']
    ]

    graph2 = [
        ['1', '1', '0', '0', '0'],
        ['1', '1', '0', '0', '0'],
        ['0', '0', '1', '0', '0'],
        ['0', '0', '0', '1', '1']
    ]

    s = Solution()
    # print(s.numIslands(graph1))
    print(s.numIslands(graph2))

    # print(g.numIslands2(matrix2))
