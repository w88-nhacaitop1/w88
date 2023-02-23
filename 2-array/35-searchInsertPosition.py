""" 35. Search Insert Position (Easy)
https://leetcode.com/problems/search-insert-position/

Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
You may assume no duplicates in the array.

*Input: [1,3,5,6], 5
*Output: 2

*Input: [1,3,5,6], 2
*Output: 1

*Input: [1,3,5,6], 7
*Output: 4

*Input: [1,3,5,6], 0
*Output: 0
"""

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1

        while left <= right:
            mid = (left + right) >> 1
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left


if __name__ == "__main__":
    nums, target = [1, 3, 5, 6], 5  # ? Output = 2

    s = Solution()
    print(s.searchInsert(nums, target))
