""" 367. Valid Perfect Square (Easy)
https://leetcode.com/problems/valid-perfect-square/

Given a positive integer num, write a function which returns True if num is a perfect square else False.

!Note: Do not use any built-in library function such as sqrt.

*Input: 16
*Output: true

*Input: 14
*Output: false """

# TODO: Approach 1: Brute Force           [O(sqrt(N)) & O(1)]
# TODO: Approach 2: Binary Search         [O(logN) & O(1)]
# TODO: Approach 3: Using Math            [O(1) & O(1)]


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i = 1
        while i * i < num:
            i += 1

        return i * i == num

    def isPerfectSquare1(self, num: int) -> bool:
        left, right = 1, num // 2

        if num == 1:
            return True

        def search(left: int, right: int, num: int) -> bool:
            while left <= right:
                mid = left + (right - left) // 2

                if mid**2 == num:
                    return True
                elif mid**2 < num:
                    return search(mid+1, right, num)
                else:
                    return search(left, mid-1, num)

            return False

        return search(left, right, num)

    def isPerfectSquare2(self, num: int) -> bool:
        return True if num**0.5 == int(num**0.5) else False

import math
if __name__ == "__main__":
    nums = [4, 9, 16, 14]
    # ? Output = [True, True, True, False]

    s = Solution()

    for num in nums:
        result = s.isPerfectSquare(num)
        result1 = s.isPerfectSquare1(num)
        result2 = s.isPerfectSquare2(num)

        print("[Approach 1] Input = {} -> Output = {}".format(num, result))
        print("[Approach 2] Input = {} -> Output = {}".format(num, result1))
        print("[Approach 3] Input = {} -> Output = {}".format(num, result2))
