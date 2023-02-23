# Maximum Sum Subarray of Size K (easy)

# Given an array of positive numbers and a positive number ‘k’, find the maximum sum of any contiguous subarray of size ‘k’.

# Input: [2, 1, 5, 1, 3, 2], k=3
# Output: 9
# Explanation: Subarray with maximum sum is [5, 1, 3].

# Input: [2, 3, 4, 1, 5], k=2
# Output: 7
# Explanation: Subarray with maximum sum is [3, 4].

# TODO: Approach 1: Sliding Window          [O(N) & O(K)]

from typing import List


class Solution:
    def maxSum(self, nums: List[int], K: int) -> int:
        result = 0
        windowStart = 0
        _sum = 0

        for windowEnd in range(len(nums)):
            _sum += nums[windowEnd]

            if windowEnd >= K - 1:
                result = max(result, _sum)

                _sum -= nums[windowStart]
                windowStart += 1

        return result


if __name__ == "__main__":
    # nums, K = [2, 1, 5, 1, 3, 2], 3
    nums, K = [2, 3, 4, 1, 5], 2
    
    s = Solution()
    print(s.maxSum(nums, K))

