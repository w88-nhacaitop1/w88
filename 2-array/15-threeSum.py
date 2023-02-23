""" 15. 3Sum (Medium)
https://leetcode.com/problems/3sum/

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

!Note:
!The solution set must not contain duplicate triplets.

*Given array nums = [-1, 0, 1, 2, -1, -4],

*A solution set is:
*    [
*      [-1, 0, 1],
*      [-1, -1, 2]
*    ] 
"""

# TODO: Approach 1: Brute Force             [O(N^3) & O(1)]
# TODO: Approach 2: Using Hash Table        [O(N^2) & O(N)]
# TODO: Approach 3: Using Two Pointers      [O(N^2) & O(1)]

from typing import List


class Solution:
    def threeSum3(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return None

        ans = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                pass
            else:
                left = i + 1
                right = len(nums) - 1

                while left < right:
                    _sum = nums[i] + nums[left] + nums[right]
                    if _sum == 0:
                        ans.append([nums[i], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < len(nums) - 1 and nums[left] == nums[left-1]:
                            left += 1
                        while right > 0 and nums[right] == nums[right+1]:
                            right -= 1
                    elif _sum < 0:
                        left += 1
                    else:
                        right -= 1

        return ans


if __name__ == "__main__":
    # nums = [-1, 0, 1, 2, -1, -4]  # ? Output = []
    # nums = [-2, 0, 0, 2, 2]   # ? Output = []
    nums = [0, 0, 0]  # ? Output = []

    # test = (1 + 9) >> 1  # ? Output: 1010 >> 1 == 0101

    s = Solution()
    print(s.threeSum3(nums))
