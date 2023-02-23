""" 4. Median of Two Sorted Arrays (Hard)
https://leetcode.com/problems/median-of-two-sorted-arrays/
https://www.geeksforgeeks.org/find-median-of-list-in-python/

There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
You may assume nums1 and nums2 cannot be both empty.

*nums1 = [1, 3]
*nums2 = [2]
*The median is 2.0

*nums1 = [1, 2]
*nums2 = [3, 4]
*The median is (2 + 3)/2 = 2.5
 """
# TODO: Approach 1: Using sorted()                       [O(NlogN) & O(N)]
# TODO: Approach 2: Using Interactive Solution           [O(log(min(x,y))) & O[1]]
# *Time complexity: O(log(min(x, y))), where x and y are lengths of nums1 & nums2.
# *1. Pick the shorter array to binary search on, as it would take more time to partition the longer array.
# *2. Set max and min for left and right partitions on both arrays (set to -inf and +inf when partition is empty).
# *3. If all elements on the arrays on the left are smaller than those on the right, return the median based on the parity of combined length of the input arrays.
# *4. If we cut the partition too deep into the right side, move the pivot toward the left.
# *     And vice versa until we reach a point where all elements in left partitions are smaller than all elements in the right partitions.


from typing import List


class Solution:
    def findMedianSortedArray1(self, nums1: List[int], nums2: List[int]) -> float:
        nums = sorted(nums1 + nums2)
        len12 = len(nums)

        if len12 % 2:  # ~~ len12 % 2 != 0
            return (nums[len12//2])
        else:
            return (nums[len12//2] + nums[len12//2 - 1]) / 2

    def findMedianSortedArray2(self, nums1: List[int], nums2: List[int]) -> float:
        len1, len2 = len(nums1), len(nums2)

        # We need to have nums1 as smaller in length
        if len1 > len2:
            return self.findMedianSortedArray2(nums2, nums1)

        low, high = 0, len1
        while low <= high:
            part1 = (low + high) // 2
            part2 = (len1 + len2 + 1) // 2 - part1

            maxLeft1 = nums1[part1 - 1] if part1 != 0 else float("-inf")
            minRight1 = nums1[part1] if part1 != len1 else float("inf")
            maxLeft2 = nums2[part2 - 1] if part2 != 0 else float("-inf")
            minRight2 = nums2[part2] if part2 != len2 else float("inf")

            if (maxLeft1 <= minRight2 and
                    maxLeft2 <= minRight1):

                if (len1 + len2) % 2:   # ~~ (len1 + len2) % 2 != 0:
                    return max(maxLeft1, maxLeft2)
                else:
                    return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2

            elif maxLeft1 > minRight2:
                high = part1 - 1
            else:
                low = part1 + 1


if __name__ == "__main__":
    # nums1 = [1, 3]
    # nums2 = [2]

    # nums1 = [1, 2]
    # nums2 = [3, 4]

    # nums1 = [1, 2, 3]
    # nums2 = [4, 5]

    # nums1 = [2, 4, 6]
    # nums2 = [1, 3, 5]

    nums1 = [1, 2, 3]
    nums2 = [4, 5, 10]

    s = Solution()
    # print(s.findMedianSortedArray1(nums1, nums2))
    print(s.findMedianSortedArray2(nums1, nums2))
