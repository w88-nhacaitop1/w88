""" 383. Ransom Note (Easy) Microsoft
https://leetcode.com/problems/ransom-note/

Given an arbitrary ransom note string and another string containing letters from all the magazines. 
Write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.
Each letter in the magazine string can only be used once in your ransom note.

!Note:
!You may assume that both strings contain only lowercase letters.

*   canConstruct("a", "b") -> false
*   canConstruct("aa", "ab") -> false
*   canConstruct("aa", "aab") -> true """

# TODO: Approach 1: Simulation - Remove character in magazine when matched (Not Recommended) - Because String is immutable value
# TODO: Approach 2: Two HashMap - Using 2 Counter in python                   [O(N) & O(k)] - M: length ransomNote, N: length magazine (N > M)
# TODO: Approach 3: One HashMap - Using dict() or Counter in python           [O(N) & O(k)] - M: length ransomNote, N: length magazine (N > M)
# TODO: Approach 4: Sorting and Stacks

from collections import Counter


class Solution:
    def canConstruct2(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False

        ransomNoteLetters = Counter(ransomNote)
        magazineLetters = Counter(magazine)

        for c in ransomNoteLetters.keys():
            if ransomNoteLetters[c] > magazineLetters[c]:
                return False

        return True

    def canConstruct3(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False

        letters = Counter(magazine)    # ? O(N)

        for c in ransomNote:
            if letters[c] <= 0:
                return False

            letters[c] -= 1

        return True


if __name__ == "__main__":
    # [ransomNote, magazine] = "a", "b"
    # [ransomNote, magazine] = "aa", "bb"
    # [ransomNote, magazine] = "aa", "aab"
    [ransomNote, magazine] = "fffbfg", "effjfggbffjdgbjjhhdegh"

    s = Solution()
    result2 = s.canConstruct2(ransomNote, magazine)
    result3 = s.canConstruct3(ransomNote, magazine)

    print("[Approach 2] Can Construct is {}".format(result2))
    print("[Approach 3] Can Construct is {}".format(result3))


