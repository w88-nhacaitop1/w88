""" 1394. Find Lucky Integer in an Array (Easy) Microsoft
https://leetcode.com/problems/find-lucky-integer-in-an-array/

Given an array of integers arr, a lucky integer is an integer which has a frequency in the array equal to its value.
Return a lucky integer in the array. If there are multiple lucky integers return the largest of them. 
If there is no lucky integer return -1.

*Input: arr = [2,2,3,4]
*Output: 2
Explanation: The only lucky number in the array is 2 because frequency[2] == 2.

*Input: arr = [1,2,2,3,3,3]
*Output: 3
Explanation: 1, 2 and 3 are all lucky numbers, return the largest of them.

*Input: arr = [2,2,2,3,3]
*Output: -1
Explanation: There are no lucky numbers in the array.

*Input: arr = [5]
*Output: -1

*Input: arr = [7,7,7,7,7,7,7]
*Output: 7

!Constraints:
!   1 <= arr.length <= 500
!   1 <= arr[i] <= 500
 """

from typing import List
from collections import Counter
import heapq


class Solution:
    def findLucky1(self, arr: List[int]) -> int:
        result = -1
        count = Counter(arr)

        for num, count in count.items():
            if num == count:
                result = max(num, result)

        return result

    def findLucky2(self, arr: List[int]) -> int:
        nums = [0]*501
        for n in arr:
            nums[n] += 1

        for i in range(len(nums)-1, 0, -1):
            if nums[i] == i:
                return i

        return -1


if __name__ == "__main__":
    nums = [2, 2, 2, 3, 3]

    s = Solution()
    result = s.findLucky(nums)

    print("[Approach] Result is {}".format(result))
