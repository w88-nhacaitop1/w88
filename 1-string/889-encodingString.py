"""
This problem was asked by Amazon. (Easy)

Run-length encoding is a fast and simple method of encoding strings.
The basic idea is to represent repeated successive characters as a single count and character.

*For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

Implement run-length encoding and decoding.
You can assume the string to be encoded have no digits and consists solely of alphabetic characters.
You can assume the string to be decoded is valid.
"""

# TODO: Approach 1: Sliding Window      [O(N) & O(1)]

class Solution:
    def encodingString(self, s: str) -> str:
        left, right = 1, 0
        result = ""

        while right < len(s):
            count = 1
            while left < len(s) and s[right] == s[left]:
                count += 1
                left += 1

            result += "{0}{1}".format(count, s[right])
            right = left
            left = right + 1

        return result


if __name__ == "__main__":
    s = Solution()
    inputStr = "AAAABBBCCDAA"  # ? Output = "4A3B2C1D2A"
    result = s.encodingString(inputStr)
    print("The string \"{0}\" would be encoded as \"{1}\"".format(
        inputStr, result))
