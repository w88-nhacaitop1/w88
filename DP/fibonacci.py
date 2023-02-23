

# TODO: Approach 1: Brute Force with Recursion      [O(2^n) & O(1)]
# TODO: Approach 2: Top-down with Memoization       [O(n) & O(n)]
# TODO: Approach 3: Bottom-up with Tabulation       [O(n) & O(n)]
# TODO: Approach 4: Bottom-up without Tabulation    [O(n) & O(1)]

from typing import List


class Solution:
    def calculateFibonacci1(self, n: int) -> int:
        if n < 2:
            return n

        return self.calculateFibonacci1(n - 1) + self.calculateFibonacci1(n-2)

    def calculateFibonacci2(self, n: int) -> List[int]:
        memoize = [-1 for x in range(n+1)]

        return self.calculateFibonacciRecur(memoize, n)

    def calculateFibonacciRecur(self, memoize: List[int], n: int) -> int:
        if n < 2:
            return n

        if memoize[n] > 0:
            return memoize[n]

        memoize[n] = self.calculateFibonacciRecur(
            memoize, n - 1) + self.calculateFibonacciRecur(memoize, n - 2)

        return memoize[n]

    def calculateFibonacci3(self, n: int) -> int:
        if n < 2:
            return n

        memoize = [0]*n
        memoize[0] = 0
        memoize[1] = 1

        for i in range(2, n):
            memoize[i] = memoize[i-1] + memoize[i-2]

        return memoize[n - 1] + memoize[n-2]

    def calculateFibonacci4(self, n: int) -> int:
        if n < 2:
            return n
        
        a, b = 0, 1
        for _ in range(2, n):
            c = a + b
            a = b
            b = c

        return a + b

if __name__ == "__main__":
    num = 8

    s = Solution()
    # print(s.calculateFibonacci1(num))
    # print(s.calculateFibonacci2(num))
    # print(s.calculateFibonacci3(num))
    # print(s.calculateFibonacci4(num))
