""" 1089. Duplicate Zeroes (Easy)
https://leetcode.com/problems/duplicate-zeros/

Given a fixed length array arr of integers, duplicate each occurrence of zero, shifting the remaining elements to the right.
Note that elements beyond the length of the original array are not written.
Do the above modifications to the input array in place, do not return anything from your function.

*Input: [1,0,2,3,0,4,5,0]
*Output: null
*Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]

*Input: [1,2,3]
*Output: null
*Explanation: After calling your function, the input array is modified to: [1,2,3]
 
!Note:
!1 <= arr.length <= 10000
!0 <= arr[i] <= 9
 """

from typing import List


class Solution:
    def duplicateZeroes(self, arr: List[int]) -> List[int]:
        dupZeroCount, length_ = 0, len(arr)

        # ? Step 1: Count duplicated zeroes
        for i in range(length_):
            if arr[i] == 0:
                if i < length_ - dupZeroCount - 1:
                    dupZeroCount += 1
                elif i == length_ - dupZeroCount - 1:  # ! Handle Edge case
                    length_ -= 1
                    arr[length_] = 0

        if not dupZeroCount:
            return None

        # ? Step 2: Move item, run loop from last using two-pointers
        lastIndex = length_ - dupZeroCount - 1

        for i in range(lastIndex, -1, -1):
            if arr[i] == 0:
                arr[i + dupZeroCount] = 0
                dupZeroCount -= 1
                arr[i + dupZeroCount] = 0
            else:
                arr[i + dupZeroCount] = arr[i]

        return arr


if __name__ == "__main__":
    # nums = [1, 0, 2, 3, 0, 4, 5, 0]  # ? Output = [1, 0, 0, 2, 3, 0, 0, 4]
    # nums = [1, 2, 3]  # ? Output = None
    # nums = [1, 5, 2, 0, 6, 8, 0, 6, 0] # ? Output = [1, 5, 2, 0, 0, 6, 8, 0, 0]
    nums = [8, 4, 5, 0, 0, 0, 0, 7]  # ! Output = [8, 4, 5, 0, 0, 0, 0, 0]

    s = Solution()
    result = s.duplicateZeroes(nums)

    print("Result is {}".format(result))
