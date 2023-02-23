""" 415. Add Strings (Easy)
https://leetcode.com/problems/add-strings/

Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:
The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly. """

# TODO: Approach 1: Using two pointers to keep index of 2 numbers


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i, j = len(num1)-1, len(num2)-1
        ans = ''
        carry = 0

        while i >= 0 or j >= 0 or carry:
            a = ord(num1[i]) - ord('0') if i >= 0 else 0
            b = ord(num2[j]) - ord('0') if j >= 0 else 0
            n = a + b + carry
            carry = n // 10
            ans = chr((n % 10) + ord('0')) + ans

            i, j = i-1, j-1
        return ans


if __name__ == "__main__":
    num1 = "12345667"
    num2 = "12345678"

    s = Solution()
    print(s.addStrings(num1, num2))
