""" 137. Single Number II (Medium)
https://leetcode.com/problems/single-number-ii/

Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

!Note:
!Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

* Input: [2,2,3,2]
* Output: 3

* Input: [0,1,0,1,0,1,99]
* Output: 99 """

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0

        return result


if __name__ == "__main__":
    nums = [2, 2, 3, 2]  # ? Output = 3
    # nums = [0, 1, 0, 1, 0, 1, 99] # ? Output = 99

    s = Solution()
    result = s.singleNumber(nums)

    print("Result is {}".format(result))
