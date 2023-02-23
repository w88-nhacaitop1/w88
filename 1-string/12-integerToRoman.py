# 12. Integer To Roman (Medium)
# https://leetcode.com/problems/integer-to-roman/

# Input: 3
# Output: "III"

# Input: 4
# Output: "IV"

# Input: 9
# Output: "IX"

# Input: 58
# Output: "LVIII"
# Explanation: L = 50, V = 5, III = 3.

# Input: 1994
# Output: "MCMXCIV"
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.


class Solution:
    def intToRoman(self, num: int) -> str:
        ans = ""
        Dict = {
            1: "I",
            5: "V",
            10: "X",
            50: "L",
            100: "C",
            500: "D",
            1000: "M"
        }

        i = 0
        dividend = [1000, 100, 10, 1]

        while num > 0:
            unit = num // dividend[i]

            if unit == 4:
                ans += Dict[dividend[i]] + Dict[5*dividend[i]]
            elif unit == 9:
                ans += Dict[dividend[i]] + Dict[10*dividend[i]]
            elif unit >= 5:
                ans += Dict[5*dividend[i]] + (Dict[dividend[i]] * (unit - 5))
            else:
                ans += Dict[dividend[i]] * unit
                
            num = num % dividend[i]
            i += 1

        return ans


if __name__ == "__main__":
    num = 58
    # num = 1994
    # num = 1984

    s = Solution()
    print(s.intToRoman(num))
