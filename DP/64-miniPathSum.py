""" 64. Minimum Path Sum (Medium) Amazon
https://leetcode.com/problems/minimum-path-sum/

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.
Note: You can only move either down or right at any point in time. """

# * Input:
# * [
# *   [1,3,1],
# *   [1,5,1],
# *   [4,2,1]
# * ]
# * Output: 7
# * Explanation: Because the path 1→3→1→1→1 minimizes the sum.

# TODO: Summary
# We have to find the minimum sum of numbers over a path from the top left to the bottom right of the given matrix .

# TODO: Approach 1: Brute Force                                     [O(2^m+n) & O(m+n)]
# TODO: Approach 2: Dynamic Programming 2D                          [O(mn) & O(mn)]
# TODO: Approach 3: Dynamic Programming 1D                          [O(mn) & O(n)]
# TODO: Approach 4: Dynamic Programming (Without Extra Space)       [O(mn) & O(1)]
# TODO: Approach 5: Dynamic Programming (More readable)

from typing import List
import sys


class Solution:
    def minPathSum1(self, grid: List[List[int]]) -> int:
        return self.calculate(grid, 0, 0)

    def calculate(self, grid: List[List[int]], i: int, j: int) -> int:
        print("Grid[{0}][{1}]".format(i+1, j), end="   ")
        print("Grid[{0}][{1}]".format(i, j+1))

        if (i == len(grid) or j == len(grid[0])):
            return sys.maxsize
        if (i == len(grid) - 1 and j == len(grid[0]) - 1):
            return grid[i][j]

        return grid[i][j] + min(self.calculate(grid, i + 1, j), self.calculate(grid, i, j + 1))

    def minPathSum5(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            if i > 0:
                grid[i][0] += grid[i-1][0]

        for j in range(n):
            if j > 0:
                grid[0][j] += grid[0][j-1]

        for i in range(m):
            for j in range(n):
                if i > 0 or j > 0:
                    grid[i][j] += min(grid[i-1][j], grid[i][j-1])

        return grid[m-1][n-1]


if __name__ == "__main__":
    # matrix = [
    #     [1, 3, 1],
    #     [1, 5, 1],
    #     [4, 2, 1]
    # ]

    matrix = [
        [1, 3],
        [1, 5]
    ]

    s = Solution()
    # print(s.minPathSum1(matrix))
    print(s.minPathSum5(matrix))
