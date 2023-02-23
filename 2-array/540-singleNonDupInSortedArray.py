""" 540. Single Element in a Sorted Array (Medium)
https://leetcode.com/problems/single-element-in-a-sorted-array/

You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. 
Find this single element that appears only once.

*Input: [1,1,2,3,3,4,4,8,8]
*Output: 2

*Input: [3,3,7,7,10,11,11]
*Output: 10
 
!Note: Your solution should run in O(log n) time and O(1) space.
 """

# TODO: Approach 1: Using Binary Search         [O(logN) & O(1)]


from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1

        if not nums:
            return -1

        while left < right:
            mid = left + (right - left) // 2

            if mid % 2 == 0:
                if nums[mid] == nums[mid-1]:
                    right = mid - 2
                elif nums[mid] == nums[mid+1]:
                    left = mid + 2
                else:
                    return nums[mid]
            else:
                if nums[mid] == nums[mid-1]:
                    left = mid + 1
                elif nums[mid] == nums[mid+1]:
                    right = mid - 1

        return nums[left] if left == right else -1


if __name__ == "__main__":
    nums = []
    # nums = [1, 1, 2, 2, 3, 3]  # Output = -1
    # nums = [1, 1, 2, 3, 3, 4, 4, 8, 8]  # ? Output = 2
    # nums = [1, 1, 2, 2, 3, 3, 4, 8, 8]  # ? Output = 4
    # nums = [3, 3, 7, 7, 10, 11, 11]  # ? Output = 10
    nums = [1, 1, 2, 3, 3]  # ! Output = 2 (Edge case)

    s = Solution()
    result = s.singleNonDuplicate(nums)

    print(result)
