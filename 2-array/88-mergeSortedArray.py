""" 88. Merge Sorted Array (Easy)
https://leetcode.com/problems/merge-sorted-array/

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

!Note:
!The number of elements initialized in nums1 and nums2 are m and n respectively.
!You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.

*Input:
*nums1 = [1,2,3,0,0,0], m = 3
*nums2 = [2,5,6],       n = 3

*Output: [1,2,2,3,5,6] """

# TODO: Approach 1: Brute Force                             [O((n+m)log(n+m)) & O(1)] - Bad Performance than others
# TODO: Approach 2: Two Pointers - Start from beginning     [O(n+m) & O(m)]
# TODO: Approach 3: Two Pointers - Start from end           [O(n+m) & O(1)]


class Solution:
    def merge1(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        j = 0
        for i in range(m, len(nums1)):
            if j < n:
                nums1[i] = nums2[j]
                j += 1

        nums1.sort()

    def merge2(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        pass

    def merge3(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        pass


if __name__ == "__main__":
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    m, n = 3, 3

    s = Solution()
    result1 = s.merge1(nums1, m, nums2, n)
    result2 = s.merge2(nums1, m, nums2, n)

    print("[Approach 1] Result is {}".format(result1))
    print("[Approach 2] Result is {}".format(result1))
