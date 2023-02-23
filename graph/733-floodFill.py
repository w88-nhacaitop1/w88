""" 733. Flood Fill (Easy)
https://leetcode.com/problems/flood-fill/

An image is represented by a 2-D array of integers, each integer representing the pixel value of the image(from 0 to 65535).
Given a coordinate(sr, sc) representing the starting pixel(row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.
To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, 
plus any pixels connected 4-directionally to those pixels(also with the same color as the starting pixel), and so on. 
Replace the color of all of the aforementioned pixels with the newColor.

At the end, return the modified image.

*Input:
*   image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
*   sr = 1, sc = 1, newColor = 2

*Output: [[2, 2, 2], [2, 2, 0], [2, 0, 1]]

*Explanation:
*From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected
*by a path of the same color as the starting pixel are colored with the new color.
*Note the bottom corner is not colored 2, because it is not 4-directionally connected
*to the starting pixel.

!Note:
!The length of image and image[0] will be in the range[1, 50].
!The given starting pixel will satisfy 0 <= sr < image.length and 0 <= sc < image[0].length.
!The value of each color in image[i][j] and newColor will be an integer in [0, 65535].
"""

# TODO: Approach 1: Depth First Search          (O(N) & O(N))
# TODO: Approach 2: Breadth First Search        (O(N) & O(N))

from typing import List
import collections


class Solution:
    # TODO: Approach 1: Depth First Search          (O(N) & O(N))
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        baseValue = image[sr][sc]

        def DFS(row, col, image):
            image[row][col] = newColor

            for nextRow, nextCol in [(row, col+1), (row, col-1), (row+1, col), (row-1, col)]:
                if (0 <= nextRow < len(image) and
                    0 <= nextCol < len(image[0]) and
                        image[nextRow][nextCol] == baseValue):
                    DFS(nextRow, nextCol, image)

        if baseValue != newColor:
            DFS(sr, sc, image)

        return image

    # TODO: Approach 2: Breadth First Search        (O(N) & O(N))
    def floodFill1(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        baseValue = image[sr][sc]

        def BFS(row, col, image):
            image[row][col] = newColor  # ? visited

            queue = collections.deque()
            queue.appendleft((row, col))

            while queue:
                row, col = queue.pop()
                for nextRow, nextCol in [(row, col+1), (row, col-1), (row+1, col), (row-1, col)]:
                    if (0 <= nextRow < len(image) and
                        0 <= nextCol < len(image[0]) and
                            image[nextRow][nextCol] == baseValue):
                        image[nextRow][nextCol] = newColor
                        queue.appendleft((nextRow, nextCol))

        if newColor != baseValue:
            BFS(sr, sc, image)

        return image


if __name__ == "__main__":
    image = [[0, 0, 0], [0, 1, 1]]
    image1 = [[0, 0, 0], [0, 1, 1]]
    sr, sc = 1, 1
    newColor = 1

    s = Solution()
    result = s.floodFill(image, sr, sc, newColor)
    result1 = s.floodFill1(image1, sr, sc, newColor)

    print(result)
    print(result1)
