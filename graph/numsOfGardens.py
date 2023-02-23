
""" Number of gardens (Medium)
https://github.com/quangmindx/Entrance-Test 

Van's farm has many gardens. Each garden is completely surrounded by wooden frames (left, right, above, below). 
In order to hide workers to harvest when the season comes, Van needs to know the number of gardens on his farm. 
Given an array of integer where:

Number 0: is the land of the garden
Number 1: is the wooden frames of the garden

* Example 1:
* Input:
*   arr = [
*        [0, 0, 1, 0, 0],
*        [0, 1, 0, 1, 0],
*        [0, 1, 1, 1, 0]
*    ]
* Output: 1

* Example 2:
* Input:
*   arr = [
*        [1, 1, 1, 1, 1, 1, 1],
*        [1, 0, 0, 0, 0, 0, 1],
*        [1, 0, 1, 1, 1, 0, 1],
*        [1, 0, 1, 0, 1, 0, 1],
*        [1, 0, 1, 1, 1, 0, 1],
*        [1, 0, 0, 0, 0, 0, 1],
*        [1, 1, 1, 1, 1, 1, 1]
*   ]
* Output: 2

! Constraint:
!   Input: 1 <= arr.length <= 100
!   Output: int

"""

# # TODO: Approach 2: BFS - Breath First Search         [O(M x N) & O(min(M,N))]

from typing import List


class Solution:
    def numGardens(self, arr: List[List[int]]) -> int:
        count = 0

        for row in range(len(arr)):
            for col in range(len(arr[0])):
                if arr[row][col] == 0:
                    self.BFS(row, col, arr, count)
                    print(arr)

        return count

    def BFS(self, row: int, col: int, grid: List[List[int]], count: int):
        grid[row][col] = 2  # ? Visited = 2
        queue = [(row, col)]

        while queue:
            nxt_lst = []
            for current_row, current_col in queue:
                for next_row, next_col in [(current_row, current_col+1), (current_row, current_col-1), (current_row+1, current_col), (current_row-1, current_col)]:
                    if (0 <= next_row < len(grid) and
                        0 <= next_col < len(grid[0]) and
                            grid[next_row][next_col] == 1):
                        grid[next_row][next_col] = 2
                        nxt_lst.append((next_row, next_col))
            queue = nxt_lst


if __name__ == "__main__":
    arr = [
        [0, 0, 1, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 1, 1, 1, 0],
    ]

    s = Solution()
    result1 = s.numGardens(arr)  # ? return 1

    print("Result 1 is {}".format(result1))
