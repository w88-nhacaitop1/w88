""" 75. Sort Colors (Medium)
https://leetcode.com/problems/sort-colors/

Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.
Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

*Input: [2,0,2,1,1,0]
*Output: [0,0,1,1,2,2]

Follow up:
A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
Could you come up with a one-pass algorithm using only constant space?
 """

# TODO: Approach 1: Using 3 pointers (left, mid, right)            [O(N) & O(1)]

from typing import List


class Solution:
    # Approach 1: One-pass solution
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(nums: List[int], i: int, j: int):
            temp = nums[j]
            nums[j] = nums[i]
            nums[i] = temp

        left, mid, right = 0, 0, len(nums)-1

        while mid <= right:
            if nums[mid] == 0:
                swap(nums, left, mid)
                left += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            elif nums[mid] == 2:
                swap(nums, mid, right)
                right -= 1

    # Approach 2: Two-pass solution
    def sortColors1(self, nums: List[int]) -> None:
        store = [0]*3

        for i in range(len(nums)):
            store[nums[i]] += 1

        curr, index = 0, 0
        while index < len(store) and curr < len(nums):
            if store[index] > 0:
                nums[curr] = index
                store[index] -= 1
                curr += 1
            else:
                index += 1


if __name__ == "__main__":
    # nums = [2, 0, 2, 1, 1, 0]  # ? Output = [0, 0, 1, 1, 2, 2]
    nums = [2]  # ? Output = [2]

    s = Solution()
    # s.sortColors(nums)
    s.sortColors1(nums)

    print("Result is {}".format(nums))
