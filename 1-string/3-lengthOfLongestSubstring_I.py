""" 3. Longest Substring Without Repeating Characters (Medium)
https://leetcode.com/problems/longest-substring-without-repeating-characters/
Given a string, find the length of the longest substring without repeating characters.

* Input: "abcabcbb"
* Output: 3
* Explanation: The answer is "abc", with the length of 3.

* Input: "bbbbb"
* Output: 1
* Explanation: The answer is "b", with the length of 1.
 """

# TODO: Approach 1: Brute Force                         [O(n*3) & O(1)]
# TODO: Approach 2: Sliding Window (HashMap)            [O(2n) & O(k)] - k is size of the Set
# TODO: Approach 3: Sliding Window Optimized (HashMap)  [O(n) & O(k)]
# TODO: Approach 4: Using enumerate() in Python 3       [O(n) & O(n)]


class Solution:
    # TODO: Approach 1: Brute Force                         [O(n*3) & O(1)]
    def lengthOfLongestSubstring1(self, s: str) -> int:
        def allUnique(s: str, start: int, end: int) -> bool:
            Dict = {}
            while start < end:
                char = s[start]
                if char in Dict:
                    return False
                Dict[char] = start
                start += 1
            return True

        if len(s) < 1:
            return 0

        if len(s) == 1:
            return 1

        maxLen = 1

        for i in range(len(s)-1):
            for j in range(len(s[i+1::1])):
                # sub = s[i] + s[i+1:i+j+2:1] # Bad performance
                isValid = allUnique(s, i, i + j + 1)
                if isValid and j - i + 1 > maxLen:
                    maxLen = max(j - i + 1, maxLen)

        return maxLen

    """ Sliding Windows (HashMap) """

    def lengthOfLongestSubstring2(self, s: str) -> int:
        n = len(s)
        maxLen = i = j = 0
        Dict = {}

        while i < n and j < n:
            if s[j] not in Dict:
                Dict[s[j]] = j
                j += 1
                maxLen = max(maxLen, j - i)
            else:
                del Dict[s[i]]
                i += 1

        return maxLen

    """ Using enumerate() in Python """

    def lengthOfLongestSubstring4(self, s: str) -> int:
        maxLen = j = 0
        Dicts = {}

        for i, value in enumerate(s):
            if value in Dicts:
                sums = Dicts[value] + 1
                if sums > j:
                    j = sums

            # maxLen = max(maxLen, i - start + 1)  # Maybe slow performance
            count = i - j + 1
            if count > maxLen:
                maxLen = count

            Dicts[value] = i

        return maxLen


if __name__ == "__main__":
    # input = "abcabcbb"
    # input = "abc"
    # input = "ac"
    # input = "cc"
    # input = "bbbbb"
    input = "tennhatminhnguyelnabc"  # ? Output = "atminhnguyelnabc"

    s = Solution()
    # print(s.lengthOfLongestSubstring1(input))
    print(s.lengthOfLongestSubstring2(input))
    # print(s.lengthOfLongestSubstring4(input))
