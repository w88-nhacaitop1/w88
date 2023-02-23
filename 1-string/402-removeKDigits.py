""" 
402. Remove K Digits
https://leetcode.com/problems/remove-k-digits/
 """

# TODO: Approach 1: Using Stack         [O(N+k) & O(N)] - k is nested loop with stack


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        if len(num) == k:
            return "0"

        for i in num:
            while len(stack) > 0 and stack[-1] > i and k:
                stack.pop()
                k -= 1

            stack.append(i)

        if k > 0:
            stack = stack[:-k]

        return "".join(stack).lstrip('0') or "0"


if __name__ == "__main__":
    # num, k = "1432219", 3
    # num, k = "10200", 1
    # num, k = "234891017", 6  # ? Output = 17
    num, k = "234891071", 6  # ? Output = 71
    # num, k = "112", 1

    s = Solution()
    result = s.removeKdigits(num, k)

    print(result)
