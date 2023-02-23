""" 1. Two Sum
https://leetcode.com/problems/two-sum/

Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

* Given nums = [2, 7, 11, 15], target = 9,
* Because nums[0] + nums[1] = 2 + 7 = 9,
* return [0, 1].
 """
# TODO: Approach 1: Brute Force [O(n*2) & O(1)]
# TODO: Approach 2: Two-pass HashTable [O(2n) & O(n)]
# TODO: Approach 3: One-pass HashTable [O(n) & O(n)]
# TODO: Approach 4: Using array.sort() and 2 Pointers [O(NlogN) & O(1)]

from typing import List


class Solution:
    def twoSum3(self, nums: List[int], target: int) -> List[int]:
        Dicts = {}

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in Dicts:
                return [Dicts[complement], i]
            else:
                Dicts[nums[i]] = i

        return []

    def twoSum4(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        left = 0
        right = len(nums) - 1

        while left < right:
            currentSum = nums[left] + nums[right]
            if currentSum == target:
                return [nums[left], nums[right]]
            elif currentSum < target:
                left += 1
            else:
                right -= 1

        return []


if __name__ == "__main__":
    nums, target = [2, 7, 11, 15], 9

    s = Solution()
    # print(s.twoSum3(nums, target))
    print(s.twoSum4(nums, target))
