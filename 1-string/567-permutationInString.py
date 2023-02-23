""" 567. Permutation in String (Medium)
https://leetcode.com/problems/permutation-in-string/

Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. 
In other words, one of the first string's permutations is the substring of the second string.

*Input: s1 = "ab" s2 = "eidbaooo"
*Output: True
*Explanation: s2 contains one permutation of s1 ("ba").

*Input:s1= "ab" s2 = "eidboaoo"
*Output: False

!Note:
!The input strings only contain lower case letters.
!The length of both given strings is in range [1, 10,000].
 """


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if not s1 or not s2 or len(s1) > len(s2):
            return False

        def isMatch(arr1: [], arr2: []) -> bool:
            for i in range(len(arr1)):
                if arr1[i] != arr2[i]:
                    return False

            return True

        arr1, arr2 = [0]*26, [0]*26

        for i in range(len(s1)):
            arr1[ord(s1[i]) - ord('a')] += 1

        for j in range(len(s1)):
            arr2[ord(s2[j]) - ord('a')] += 1

        start, k = 0, len(s1)

        for end in range(len(s2)-1):
            if end >= k - 1:
                if isMatch(arr1, arr2) is False:
                    arr2[ord(s2[end+1]) - ord('a')] += 1
                    arr2[ord(s2[start]) - ord('a')] -= 1
                    start += 1
                else:
                    return True

        return isMatch(arr1, arr2)


if __name__ == "__main__":
    # s1, s2 = "ab", "eidbaooo"
    # s1, s2 = "ab", "eidboaoo"
    s1, s2 = "adc", "dcda"

    s = Solution()
    result = s.checkInclusion(s1, s2)

    print("Result is {}".format(result))
