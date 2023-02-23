""" 387. First Unique Character in a String (Easy)
https://leetcode.com/problems/first-unique-character-in-a-string/

Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

*s = "leetcode"
*return 0.

*s = "loveleetcode",
*return 2.

!Note: You may assume the string contain only lowercase letters. """

# TODO: Approach 1: Loop through HashSet                        [O(N) & O(N)]
# TODO: Approach 2: Loop through enumerate() & build Counter         [O(N) & O(N)]

from collections import Counter


class Solution:
    def firstUniqChar1(self, s: str) -> int:
        if not s:
            return -1

        letters = Counter(s)        # ? O(N)
        for i in letters.keys():    # ? O(N)
            if letters[i] == 1:
                return s.find(i)

        return -1

    def firstUniqChar2(self, s: str) -> int:
        if not s:
            return -1

        letters = self.MyCounter(s)
        for idx, c in enumerate(s):
            if letters[c] == 1:
                return idx

        return -1

    def MyCounter(self, s: str) -> dict:
        dict_ = {}

        for c in s:
            if c in dict_:
                dict_[c] += 1
            else:
                dict_[c] = 1

        return dict_


if __name__ == "__main__":
    # s_ = "cc"   # ? Output = -1
    # s_ = "leetcode" # ? Output = 0
    s_ = "loveleetcode" # ? Output = 2

    s = Solution()
    print(s.firstUniqChar1(s_))
    print(s.firstUniqChar2(s_))
