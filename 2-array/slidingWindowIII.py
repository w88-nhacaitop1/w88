# Smallest Subarray with a given sum (easy)

# Given an array of positive numbers and a positive number ‘S’, find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’.
# Return 0, if no such subarray exists.

# Input: [2, 1, 5, 2, 3, 2], S=7
# Output: 2
# Explanation: The smallest subarray with a sum great than or equal to '7' is [5, 2].

# Input: [2, 1, 5, 2, 8], S=7
# Output: 1
# Explanation: The smallest subarray with a sum greater than or equal to '7' is [8].

# Input: [3, 4, 1, 1, 6], S=8
# Output: 3
# Explanation: Smallest subarrays with a sum greater than or equal to '8' are [3, 4, 1] or [1, 1, 6].

# TODO: Approach 1: Sliding Window          [O(N) & O(1)]

from typing import List
import math

class Solution:
    def smallestSum(self, nums: List[int], S: int) -> int:
        windowSum = 0
        minLength = math.inf
        windowStart = 0

        for windowEnd in range(0, len(nums)):
            windowSum += nums[windowEnd]

            while windowSum >= S:
                minLength = min(minLength, windowEnd - windowStart + 1)
                windowSum -= nums[windowStart]
                windowStart += 1

        if minLength == math.inf:
            return 0

        return minLength

if __name__ == "__main__":
    nums, S = [3, 4, 1, 1, 6], 8

    s = Solution()
    print(s.smallestSum(nums, S))

