# Given an array, find the average of all contiguous subarrays of size ‘K’ in it.

# Array: [1, 3, 2, 6, -1, 4, 1, 8, 2], K = 5
# Output: [2.2, 2.8, 2.4, 3.6, 2.8]

# TODO: Approach 1: Brute Force         [O(N*2) & O(1)]
# TODO: Approach 2: Sliding Window      [O(N) & O(1)]

from typing import List


class Solution:
    def maxAverage1(self, nums: List[int], K: 5) -> List[int]:
        results = []

        for i in range(len(nums)-K+1):
            _sum = 0.0
            for j in range(i, i+K):
                _sum += nums[j]
            results.append(_sum/K)

        return results

    def maxAverage2(self, nums: List[int], K: 5) -> List[int]:
        results = []
        windowSum, windowStart = 0.0, 0

        for windowEnd in range(len(nums)):
            windowSum += nums[windowEnd]

            if windowEnd >= K - 1:
                results.append(windowSum / K)
                windowSum -= nums[windowStart]
                windowStart += 1

        return results


if __name__ == "__main__":
    nums, K = [1, 3, 2, 6, -1, 4, 1, 8, 2], 5

    s = Solution()
    print(s.maxAverage1(nums, K))
    # print(s.maxAverage2(nums, K))
