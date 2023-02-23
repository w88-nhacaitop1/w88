# 5. Longest Palindromic Substring (Medium)
# https://leetcode.com/problems/longest-palindromic-substring/solution/

# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.

# Input:    "abacdfgdcaba"
# Output:   "abacdgfdcaba"

# TODO: Approach 1: Longest Common Substring
# TODO: Approach 2: Brute Force [O(n*3) & O(1)]
# TODO: Approach 3: Dynamic Programming [O(n*2) & O(n*2)]
# TODO: Approach 4: Expand Around Center [O(n*2) & O(1)]
# TODO: Approach 5: Manacher's Algorithm [O(n) & O(1)]

import string


def isPalindrome(s: str) -> bool:  # O(n)
    s = s.lower().replace(" ", "").translate(
        str.maketrans('', '', string.punctuation))
    return s == s[::-1]


def longestPalindrome2(s: str):
    maxLen = 0
    result = s[0] if s else ""

    if (len(s) == 1):
        return s

    for i in range(len(s)-1):
        sub = ""
        for j in range(len(s[i+1::1])):
            sub = s[i] + s[i+1:i+j+2:1] # Bad Performance
            if sub == sub[::-1] and len(sub) > maxLen:
                maxLen = max(len(sub), maxLen)
                result = sub
            elif len(s) == 2:
                return result

    return result


def longestPalindrome4(s: str) -> str:
    if not s:
        return ""

    start = 0
    end = 0

    for i in range(len(s)-1):
        len1 = expandAroundCenter(s, i, i)
        len2 = expandAroundCenter(s, i, i + 1)
        maxLen = max(len1, len2)

        if maxLen > end - start:
            start = i - (maxLen - 1) // 2
            end = i + maxLen // 2

    return s[start:end+1:1]


def expandAroundCenter(s: str, left: int, right: int) -> int:
    L = left
    R = right
    while L >= 0 and R < len(s) and s[L] == s[R]:
        L -= 1
        R += 1

    return R - L - 1


if __name__ == "__main__":
    s = "babad"
    # s = "aa"
    # s = "ac"
    # s = "cbbd"
    # s = "abcda"
    # s = "ccc"
    # s = ""
    # s = "321012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210123210012321001232100123210123"
    # s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"

    print(longestPalindrome2(s))
    # print(longestPalindrome4(s))
