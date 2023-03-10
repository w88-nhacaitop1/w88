# 167. Two Sum II - Input array is sorted
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

# Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.
# The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.
# Note:
# Your returned answers (both index1 and index2) are not zero-based.
# You may assume that each input would have exactly one solution and you may not use the same element twice.

# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.

# TODO: Approach 1: Brute Force  [O(n*2) & O(1)]
# TODO: Approach 2: One-pass Hash Table [O(n) & O(n)]
# TODO: Approach 3: Two Pointers [O(n) & O(1)]

from typing import List

class Solution:
    def twoSum3(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers)-1

        while left < right:
            totalSum = numbers[left] + numbers[right]
            if (totalSum == target):
                return [left+1, right+1]
            elif (totalSum > target):
                right -= 1
            else:
                left += 1

        return []


if __name__ == "__main__":
    numners, target = [2,7,11,15], 9

    s = Solution()
    print(s.twoSum3(numners, target))
