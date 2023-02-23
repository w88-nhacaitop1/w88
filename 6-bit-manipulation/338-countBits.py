""" 338. Counting Bits (Medium)
https://leetcode.com/problems/counting-bits/

Given an integer num, return an array of the number of 1's in the binary representation of every number in the range [0, num].

Example 1:
* Input: num = 2
* Output: [0, 1, 1]
* Explanation:
* 0 --> 0
* 1 --> 1
* 2 --> 10

Example 2:
* Input: num = 5
* Output: [0, 1, 1, 2, 1, 2]
* Explanation:
* 0 --> 0
* 1 --> 1
* 2 --> 10
* 3 --> 11
* 4 --> 100
* 5 --> 101
 
! Constraints:
! 0 <= num <= 105

"""


from typing import List
import math


class Solution:
    def countBits1(self, num: int) -> List[int]:
        result = []

        def helper(num: int) -> int:
            count = 0
            while num > 0:
                count += num % 2
                num //= 2

            return count

        for i in range(num+1):
            result.append(helper(i))

        return result

    def countBits2(self, num: int) -> List[int]:
        result = [0]*(num+1)

        for i in range(1, num+1):
            removedLastBit = i - (i & (-i))
            result[i] = result[removedLastBit] + 1

        return result


if __name__ == "__main__":
    # num = 2
    num = 5

    s = Solution()
    result1 = s.countBits1(num)
    result2 = s.countBits2(num)

    x = 5
    x &= x - 1;

    print("[Approach 1] Result is {}".format(result1))
    print("[Approach 2] Result is {}".format(result2))
