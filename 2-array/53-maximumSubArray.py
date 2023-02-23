""" 53. Maximum Subarray (Easy)
https://leetcode.com/problems/maximum-subarray/

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

*Input: [-2,1,-3,4,-1,2,1,-5,4],
*Output: 6
*Explanation: [4,-1,2,1] has the largest sum = 6.

?Follow up:
?If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
 """

# TODO: Approach 0: Brute Force (2 nested loops)                [O(N^2) & O(1)]
# TODO: Approach 1: Divide and Conquer                          [O(NlogN) & O(logN)]
# TODO: Approach 2: Greedy                                      [O(N) & O(1)]
# TODO: Approach 3: Dynamic Programming (Kadane's algorithm)    [O(N) & O(1)]

from typing import List
import math


class Solution:
    def maxSubArray1(self, nums: List[int]) -> int:
        max_sum = 0

        return max_sum

    def maxSubArray2(self, nums: List[int]) -> int:
        local_sum, global_sum = 0, -math.inf

        for i in range(len(nums)):
            local_sum = max(nums[i], nums[i] + local_sum)
            global_sum = max(global_sum, local_sum)

        return global_sum

    def maxSubArray3(self, nums: List[int]) -> int:
        n = len(nums)
        max_sum = nums[0]

        for i in range(n):
            if nums[i - 1] > 0:
                nums[i] += nums[i-1]

            max_sum = max(nums[i], max_sum)

        return max_sum


if __name__ == "__main__":
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]  # ? Output = 6

    s = Solution()
    result1 = s.maxSubArray1(nums)
    result2 = s.maxSubArray2(nums)
    result3 = s.maxSubArray3(nums)

    print("[Approach 1] Result is {}".format(result1))
    print("[Approach 2] Result is {}".format(result2))
    print("[Approach 3] Result is {}".format(result3))
