""" 476. Number Complement (Easy)
https://leetcode.com/problems/number-complement/

Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.

* Input: 5
* Output: 2
* Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.
 
* Input: 1
* Output: 0
* Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.
 
!Note:
!The given integer is guaranteed to fit within the range of a 32-bit signed integer.
!You could assume no leading zero bit in the integer's binary representation.
!This question is the same as 1009: https://leetcode.com/problems/complement-of-base-10-integer/ """

# TODO: Approach 1: Flip Bit by Bit                                         [O(1) & O(1)] - O(1) since we're doing not more than 32 iterations here.
# TODO: Approach 2: Compute Bit Length and Construct 1-bits Bitmask         [O(1) & O(1)]
# TODO: Approach 3: Built-in Functions to Construct 1-bits Bitmask          [O(1) & O(1)]
# TODO: Approach 4: highestOneBit OpenJDK algorithm from Hacker's Delight   [O(1) & O(1)]


class Solution:
    def findComplement1(self, num: int) -> int:
        p, bit = num, 1

        while p:
            num ^= bit
            bit <<= 1
            p >>= 1

        return num

    def findComplement3(self, num: int) -> int:
        result = (1 << num.bit_length()) - 1 - num
        return result


if __name__ == "__main__":
    num = 10  # ? Output = 5
    # num = 5  # ? Output = 2
    # num = 1 # ? Output = 0

    s = Solution()
    result1 = s.findComplement1(num)
    result3 = s.findComplement3(num)

    print("[Approach 1] Result is {}".format(result1))
    print("[Approach 3] Result is {}".format(result3))
