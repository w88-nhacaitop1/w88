""" 1035. Uncrossed Lines (Medium)
https://leetcode.com/problems/uncrossed-lines/

! This problem is equivalent to longest common subsequence

 """

# TODO: Approach 1: 2D Dynamic programming          [O(MxN) & O(1)]
# TODO: Approach 2: Recursion with memoization      [O()]

from typing import List


class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        M, N = len(A), len(B)
        dp = [[0 for _ in range(N+1)] for _ in range(M+1)]

        for i in range(M):
            for j in range(N):
                if A[i] == B[j]:
                    dp[i+1][j+1] = 1 + dp[i][j]
                else:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])

        return dp[-1][-1]


if __name__ == "__main__":
    # A = [1, 4, 2]
    # B = [1, 2, 4]
    # ? Output = 2

    A = [2, 5, 1, 2, 5]
    B = [10, 5, 2, 1, 5, 2]
    # ? Output = 3

    s = Solution()
    result = s.maxUncrossedLines(A, B)

print("Result is {}".format(result))
