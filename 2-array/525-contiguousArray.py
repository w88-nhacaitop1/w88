""" 525. Contiguous Array (Medium)
https://leetcode.com/problems/contiguous-array/
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

*Input: [0,1]
*Output: 2
*Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.

*Input: [0,1,0]
*Output: 2
*Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

!Note: The length of the given binary array will not exceed 50,000.
 """

# TODO: Approach 1: Brute Force (Time Limit Exceeded)           [O(N^2) & O(1)]
# TODO: Approach 2: Using HashTable                             [O(N) & O(N)]

from typing import List


class Solution:
    def findMaxLength1(self, nums: List[int]) -> int:
        result = 0
        for i in range(len(nums)-1):
            count = -1
            for j in range(i+1, len(nums)):
                if nums[j] == 1:
                    count += 1
                else:
                    count -= 1

                if count == 0:
                    result = max(result, j - i + 1)

        return result

    def findMaxLength2(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
            
        count, maxLen = 0, 0
        dicts = {0:-1}

        for i in range(len(nums)):
            count = count + 1 if nums[i] == 1 else count - 1
            if count in dicts:
                maxLen = max(maxLen, i - dicts[count])
            else:
                dicts[count] = i

        return maxLen


if __name__ == "__main__":
    # nums = [1]
    nums = [0, 1]  # ? Output = 2
    # nums = [0, 1, 0]  # ? Output = 2
    # nums = [0, 1, 1]  # ? Output = 2
    # nums = [0, 1, 0, 1]  # ? Output = 4
    # nums = [0, 1, 0, 0, 1, 1, 0]  # ? Output = 6
    # nums = [0, 0, 1, 0, 0, 0, 1, 1]  # ? Output = 6

    s = Solution()
    result = s.findMaxLength2(nums)

    print("Result is {}".format(result))
