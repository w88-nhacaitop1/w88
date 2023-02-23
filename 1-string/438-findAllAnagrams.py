""" 438. Find All Anagrams in a String (Medium)
https://leetcode.com/problems/find-all-anagrams-in-a-string/

Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.
The order of output does not matter.

*Input: s: "cbaebabacd" p: "abc"
*Output: [0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

*Input: s: "abab" p: "ab"
*Output: [0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
 """


from collections import Counter
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        lengthP, lengthS = len(p), len(s)
        if not s or not p or lengthS < lengthP:
            return []

        def checkAnagrams(arrS: [], arrP: []) -> bool:
            for i in range(len(arrP)):
                if arrP[i] != arrS[i]:
                    return False

            return True

        arrS = [0]*26   # "cbaebabacd"
        arrP = [0]*26   # "abc"
        startWindow = 0
        result = []

        for i in range(lengthP):
            arrS[ord(s[i]) - ord('a')] += 1

        for j in range(lengthP):
            arrP[ord(p[j]) - ord('a')] += 1

        for endWindow in range(len(s)-1):
            if endWindow >= lengthP - 1:
                if checkAnagrams(arrS, arrP):
                    result.append(startWindow)

                arrS[ord(s[startWindow]) - ord('a')] -= 1
                arrS[ord(s[endWindow+1]) - ord('a')] += 1
                startWindow += 1

        if checkAnagrams(arrS, arrP):
            result.append(lengthS - lengthP)

        return result


if __name__ == "__main__":
    # s, p = "cbaebabacd", "abc"
    s, p = "abab", "ab"

    solution = Solution()
    result = solution.findAnagrams(s, p)

    print(result)
