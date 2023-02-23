# 125. Valid Palindrome (Easy)
# https://leetcode.com/problems/valid-palindrome/

# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
# Note: For the purpose of this problem, we define empty string as valid palindrome.

# Input: "A man, a plan, a canal: Panama"
# Output: true

# Input: "race a car"
# Output: false

from distutils.log import debug
import string

class Solution:
    def isPalindrome(self, s:str) -> bool:
        s = s.lower().replace(" ", "").translate(str.maketrans('', '', string.punctuation))

        return s == s[::-1]

if __name__ == "__main__":
    # input = "A man, a plan, a canal: Panama"
    input = "race a car"

    s = Solution()
    result = s.isPalindrome(input)

    test = 1 ^ 2 ^ 2

    if result:
        print("True")
    else:
        print("False")