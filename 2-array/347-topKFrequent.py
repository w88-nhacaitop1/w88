""" 347. Top K Frequent Elements (Medium)
https://leetcode.com/problems/top-k-frequent-elements/

Given a non-empty array of integers, return the k most frequent elements.

*Input: nums = [1,1,1,2,2,3], k = 2
*Output: [1,2]

*Input: nums = [1], k = 1
*Output: [1]

!Note:
!You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
!Your algorithm's time complexity must be better than O(n log n), where n is the array's size. """

# TODO: Approach 1: Using Heap (built-in heapq)         [O(Nlog(k)) & O(N)]
# TODO: Approach 2: Build a Heap

from typing import List
from collections import Counter
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)   # ? O(N)
        # ? Nlog(k) - Build Heap & output list
        return heapq.nlargest(k, count.keys(), key=count.get)


if __name__ == "__main__":
    nums, k = [1, 1, 1, 2, 2, 3], 2

    s = Solution()
    print(s.topKFrequent(nums, k))
