
""" 283. Move Zeroes(Easy)
https://leetcode.com/problems/move-zeroes/

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

* Input: [0, 1, 0, 3, 12]
* Output: [1, 3, 12, 0, 0]

!Note:
!You must do this in-place without making a copy of the array.
!Minimize the total number of operations.
 """

# TODO: Approach 2: Combine in two loops            [O(N) & O(1)]
# TODO: Approach 3: Combine in one loop             [O(N) & O(1)]

from typing import List


class Solution:
    # TODO: Approach 2: Combine in two loops            [O(N) & O(1)]
    def moveZeroes2(self, nums: List[int]):
        lastZeroIndex = 0

        for i in range(len(nums)):
            if (nums[i] != 0):
                nums[lastZeroIndex] = nums[i]
                lastZeroIndex += 1

        for i in range(lastZeroIndex, len(nums)):
            nums[i] = 0

    # TODO: Approach 3: Combine in one loop             [O(N) & O(1)]
    def moveZeroes3(self, nums: List[int]):
        lastZeroIndex = 0

        for i in range(len(nums)):
            if (nums[i] != 0):
                nums[lastZeroIndex] ^= nums[i]
                nums[i] ^= nums[lastZeroIndex]
                nums[lastZeroIndex] ^= nums[i]

                lastZeroIndex += 1


if __name__ == "__main__":
    nums2 = [0, 1, 0, 3, 12]  # ? Output = [1, 3, 12, 0, 0]
    nums3 = [0, 1, 0, 3, 12]  # ? Output = [1, 3, 12, 0, 0]

    s = Solution()
    s.moveZeroes2(nums2)
    s.moveZeroes3(nums3)

    print("[Approach 2] Result is {}".format(nums2))
    print("[Approach 3] Result is {}".format(nums3))
