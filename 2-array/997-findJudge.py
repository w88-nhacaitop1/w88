""" 997. Find the Town Judge (Easy) - Amazon
https://leetcode.com/problems/find-the-town-judge/

In a town, there are N people labelled from 1 to N.  There is a rumor that one of these people is secretly the town judge.
If the town judge exists, then:
    !The town judge trusts nobody.
    !Everybody(except for the town judge) trusts the town judge.
    There is exactly one person that satisfies properties 1 and 2.
    You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a trusts the person labelled b.
If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.

*Input: N = 2, trust = [[1,2]]
*Output: 2

*Input: N = 3, trust = [[1,3],[2,3]]
*Output: 3

*Input: N = 3, trust = [[1,3],[2,3],[3,1]]
*Output: -1

*Input: N = 3, trust = [[1,2],[2,3]]
*Output: -1

*Input: N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
*Output: 3
 
!Note:
!1 <= N <= 1000
!trust.length <= 10000
!trust[i] are all different
!trust[i][0] != trust[i][1]
!1 <= trust[i][0], trust[i][1] <= N
 """

from typing import List


class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        trustedCount = {}

        if not trust:
            return N

        for i, j in trust:
            trustedCount[i] = trustedCount[i] - 1 if i in trustedCount else -1
            trustedCount[j] = trustedCount[j] + 1 if j in trustedCount else 1

        for num in range(1, N + 1):
            if num in trustedCount and trustedCount[num] == N - 1:
                return num

        return -1


if __name__ == "__main__":
    # N, trust = 1, []  # ? Output = 2
    # N, trust = 2, [[1, 2]]  # ? Output = 2
    # N, trust = 2, [[1, 2], [2, 1]]  # ? Output = -1
    # N, trust = 4, [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]  # ? Output = 3
    N, trust = 11, [[1, 8], [1, 3], [2, 8], [2, 3], [4, 8], [4, 3], [5, 8], [
        5, 3], [6, 8], [6, 3], [7, 8], [7, 3], [9, 8], [9, 3], [11, 8], [11, 3]]

    s = Solution()
    result = s.findJudge(N, trust)

    print("Result is {}".format(result))
