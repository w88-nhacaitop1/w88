# Amazon | OA 2019 | Two Sum - Unique Pairs
# https://leetcode.com/discuss/interview-question/372434

# Given an int array nums and an int target, find how many unique pairs in the array such that their sum is equal to target. Return the number of pairs.

# Input: nums = [1, 1, 2, 45, 46, 46], target = 47
# Output: 2
# Explanation:
# 1 + 46 = 47
# 2 + 45 = 47

# Input: nums = [1, 1], target = 2
# Output: 1
# Explanation:
# 1 + 1 = 2

# Input: nums = [1, 5, 1, 5], target = 6
# Output: 1
# Explanation:
# [1, 5] and [5, 1] are considered the same.

# TODO: Approach 1: Brute Force         
# TODO: Approach 2: Using set()         [O(N) & O(N)]       https://www.geeksforgeeks.org/python-set-method/
# TODO: Approach 3: Sort & Two Pointers [O(NlogN) & O(N)]

from typing import List

class Solution:
    def uniqueTwoSum2(self, nums: List[int], target: int) -> int:
        ans, comp = set(), set()

        for n in nums:
            c = target - n
            if c in comp:
                res = (n, c) if n > c else (c, n)
                if res not in ans:
                    ans.add(res)
            
            comp.add(n)

        return len(ans)

    def uniqueTwoSum3(self, nums: List[int], target: int) -> int:
        nums.sort()

        left, right = 0, len(nums) - 1
        res = 0

        while left < right:
            totalSum = nums[left] + nums[right]
            if totalSum < target:
                left += 1
            elif totalSum > target:
                right -= 1
            else:
                res += 1
                vLeft, vRight = nums[left], nums[right]
                while left < right and nums[left] == vLeft:
                    left += 1
                while left < right and nums[right] == vRight:
                    right -= 1

        return res

if __name__ == "__main__":
    nums, target = [1, 1, 2, 45, 46, 46], 47

    s = Solution()
    print(s.uniqueTwoSum2(nums, target))
    print(s.uniqueTwoSum3(nums, target))





