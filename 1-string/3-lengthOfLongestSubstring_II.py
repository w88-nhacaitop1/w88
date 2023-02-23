""" Longest Substring with K Distinct Characters (Medium)
https://www.educative.io/courses/grokking-the-coding-interview/YQQwQMWLx80

Given a string, find the length of the longest substring in it with no more than K distinct characters.

*Input: String="araaci", K=2
*Output: 4
*Explanation: The longest substring with no more than '2' distinct characters is "araa".

*Input: String="araaci", K=1
*Output: 2
*Explanation: The longest substring with no more than '1' distinct characters is "aa".

*Input: String="cbbebi", K=3
*Output: 5
*Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi". """

# TODO: Approach 1: Sliding Window          [O(n+n) & O(n)]


class Solution:
    def lengthOfLongestSubstring1(self, s: str, K: int) -> int:
        j = 0
        maxLen = 0
        Dicts = {}

        for i in range(len(s)):
            if s[i] not in Dicts:
                Dicts[s[i]] = 0
            Dicts[s[i]] += 1

            while len(Dicts) > K:
                Dicts[s[j]] -= 1
                if Dicts[s[j]] == 0:
                    del Dicts[s[j]]
                j += 1

            maxLen = max(maxLen, i - j + 1)
        return maxLen


if __name__ == "__main__":
    # inputs, K = "araaci", 2
    # inputs, K = "araaci", 1
    inputs, K = "cbbebi", 3

    s = Solution()
    print(s.lengthOfLongestSubstring1(inputs, K))
