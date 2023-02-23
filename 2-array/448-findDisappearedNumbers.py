""" 448. Find All Numbers Disappeared in an Array (Easy)
https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

Given an array nums of n integers where nums[i] is in the range [1, n], 
return an array of all the integers in the range [1, n] that do not appear in nums.

*Example 1:
*   Input: nums = [4,3,2,7,8,2,3,1]
*   Output: [5,6]

*Example 2:
*   Input: nums = [1,1]
*   Output: [2] 

!Constraints:
!   n == nums.length
!   1 <= n <= 105
!   1 <= nums[i] <= n

? Follow up: Could you do it without extra space and in O(n) runtime? 
? You may assume the returned list does not count as extra space.
"""

# TODO: Approach 1: Using HashMap [O(N) & O(N)]
# TODO: Approach 2: Based on Constraint, we use negative number to check visited index in array [O(N) & O(1)]

from typing import List


class Solution:
    def findDisappearedNumbers1(self, nums: List[int]) -> List[int]:
        hash_table = {}
        result = []

        for num in nums:
            hash_table[num] = 1

        for num in range(1, len(nums)+1):
            if num not in hash_table:
                result.append(num)

        return result

    # TODO: Approach 2: Based on Constraint, we use negative number to check visited index in array [O(N) & O(1)]

    def findDisappearedNumbers2(self, nums: List[int]) -> List[int]:
        for num in nums:
            new_index = abs(num) - 1
            if nums[new_index] > 0:
                nums[new_index] *= -1

        # ? Reference: https://stackoverflow.com/questions/6475314/python-for-in-loop-preceded-by-a-variable
        return [i+1 for i in range(len(nums)) if nums[i] > 0]


if __name__ == "__main__":
    nums = [4, 3, 2, 7, 8, 2, 3, 1]  # ? Output: [5,6]

    s = Solution()
    result1 = s.findDisappearedNumbers1(nums)
    result2 = s.findDisappearedNumbers2(nums)

    print("Result 1 is {}".format(result1))
    print("Result 2 is {}".format(result2))
