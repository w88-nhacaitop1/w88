""" 973. K Closest Points to Origin
https://leetcode.com/problems/k-closest-points-to-origin/

We have a list of points on the plane.  Find the K closest points to the origin (0, 0).
(Here, the distance between two points on a plane is the Euclidean distance.)
You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)

*Input: points = [[1,3],[-2,2]], K = 1
*Output: [[-2,2]]
Explanation: 
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].

*Input: points = [[3,3],[5,-1],[-2,4]], K = 2
*Output: [[3,3],[-2,4]]
(The answer [[-2,4],[3,3]] would also be accepted.)
 

!Note:
!   1 <= K <= points.length <= 10000
!   -10000 < points[i][0] < 10000
!   -10000 < points[i][1] < 10000
"""

from typing import List
from math import sqrt
from collections import Counter
import heapq


class Solution:
    def kClosest1(self, points: List[List[int]], K: int) -> List[List[int]]:
         return sorted(points, key=lambda i: pow(i[0],2) + pow(i[1],2))[:K]

    def kClosest2(self, points: List[List[int]], K: int) -> List[List[int]]:
        return heapq.nsmallest(K, points, key=lambda i: pow(i[0],2) + pow(i[1],2))

if __name__ == "__main__":
    points, K = [[1, 3], [-2, 2]], 1            # ? Output = [[-2,2]]
    # points, K = [[3, 3], [5, -1], [-2, 4]], 2   # ? Output = [[3,3],[-2,4]]

    s = Solution()
    result1 = s.kClosest1(points, K)
    result2 = s.kClosest2(points, K)

    print("[Approach 1] Result is {}".format(result1))
    print("[Approach 2] Result is {}".format(result2))
