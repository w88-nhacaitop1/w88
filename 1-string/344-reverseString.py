""" 344. Reverse String (Easy)
https://leetcode.com/problems/reverse-string/

Write a function that reverses a string. The input string is given as an array of characters char[].
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
You may assume all the characters consist of printable ascii characters.

*Input: ["h","e","l","l","o"]
*Output: ["o","l","l","e","h"]

*Input: ["H","a","n","n","a","h"]
*Output: ["h","a","n","n","a","H"]
"""

# TODO: Approach: Using Two Pointers         [O(N) & O(1)]

from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s)-1
        while left < right:
            temp = s[right]
            s[right] = s[left]
            s[left] = temp

            left += 1
            right -= 1


if __name__ == "__main__":
    inputs = ["h", "e", "l", "l", "o"]  # ? Output = ['o', 'l', 'l', 'e', 'h']

    s = Solution()
    s.reverseString(inputs)

    print(inputs)
