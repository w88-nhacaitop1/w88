# 13. Roman to Integer (Easy)
# https://leetcode.com/problems/roman-to-integer/

# Input: "III"
# Output: 3

# Input: "IV"
# Output: 4

# Input: "IX"
# Output: 9

# Input: "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.

# Input: "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

# TODO: Do substraction if next element s[i+1] is larger than the current one s[i]
# (for example IV, current element is I, next element is V, the answer is 5-1=4)
# TODO: Approach 1: Brute Force         [O(N) & O(1)]

class Solution:
    def romanToInt(self, s: str) -> int:
        number = 0
        i = 0
        Dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        while i < len(s) - 1:
            n1 = Dict[s[i]]
            n2 = Dict[s[i+1]]
            if (n1 < n2):
                number += n2 - n1
                i += 1
            else:
                number += n1
            
            i += 1

        if Dict[s[len(s) - 1]] <= Dict[s[len(s) - 2]]:
            number += Dict[s[len(s) - 1]]

        return number


if __name__ == "__main__":
    # input = "I"
    # input = "III"
    # input = "IV"
    input = "LVIII"
    # input = "MCMXCIV"

    s = Solution()
    print(s.romanToInt(input))
