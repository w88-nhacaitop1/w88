""" Migratory Birds
https://www.hackerrank.com/challenges/migratory-birds/problem
 """

# TODO: Approach 1: Using heapq         [O(N + klog(N)) & O(N)]
# TODO: Approach 2: Using Dict          [O(N) & O(N)]

from typing import List
from collections import Counter
import heapq


class Solution:
    def migratoryBirds1(self, arr: List[int]) -> int:
        count = Counter(arr)    # ? O(N)
        result = heapq.nlargest(1, count.keys(), key=count.get)  # ? O(klog(N))

        return result[0] if result else None

    def migratoryBirds2(self, arr: List[int]) -> int:
        maxCount = 0
        maxItem = 0
        Dict = {}

        for i in arr:
            if i in Dict:
                Dict[i] += 1
            else:
                Dict[i] = 1

            if Dict[i] > maxCount:
                maxCount = Dict[i]
                maxItem = i

        return maxItem


if __name__ == "__main__":
    arr = [1, 4, 4, 4, 5, 3]  # ? Output = 3

    s = Solution()
    print("Result 1: {}".format(s.migratoryBirds1(arr)))
    print("Result 2: {}".format(s.migratoryBirds2(arr)))
