# 8. String To Integer (Medium)
# https://leetcode.com/problems/string-to-integer-atoi/

# TODO: Approach 1: Using Regex
# TODO: Approach 2: Brute Force without using Regex


class Solution:
    def myAtoi1(self, s: str) -> int:
        import re
        match = re.search(r"^\s*[\-\+]?\d+", s)

        if match:
            match = int(match.group(0))
            low = -pow(2, 31)
            high = pow(2, 31) - 1
            if match >= high:
                return high
            elif match < low:
                return low
            else:
                return match
        else:
            return 0


if __name__ == "__main__":
    # value = "42"
    # value = "   -42"
    value = "4193 with words"


    s = Solution()
    print(s.myAtoi1(value))
