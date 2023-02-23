
""" 9. Palindrome Number (Easy)
https://leetcode.com/problems/palindrome-number/description/

Given an integer x, return true if x is palindrome integer.
An integer is a palindrome when it reads the same backward as forward.
For example, 121 is a palindrome while 123 is not.
"""
# * Example 1:
# * Input: x = 121
# * Output: true
# * Explanation: 121 reads as 121 from left to right and from right to left.

# TODO: Approach 1: Brute Force - Convert to string [O(N) & O(1)]
# TODO: Approach 2: Optimized - Resolve without converting the integer to string [O(N) & O(1)]


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x != 0 and x % 10 == 0):
            return False

        reversedNumber = 0
        while x > reversedNumber:
            reversedNumber = reversedNumber * 10 + x % 10
            x //= 10

        return x == reversedNumber or x == reversedNumber//10


if __name__ == "__main__":
    s = Solution()

    x = 11  # ? Output: true
    result = s.isPalindrome(x)

    print("Result is {0}".format(result))
