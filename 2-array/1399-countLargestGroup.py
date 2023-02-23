""" 1399. Count Largest Group (Easy)
https://leetcode.com/problems/count-largest-group/

Given an integer n. Each number from 1 to n is grouped according to the sum of its digits. 
Return how many groups have the largest size.

*Input: n = 13
*Output: 4
*Explanation: There are 9 groups in total, they are grouped according sum of its digits of numbers from 1 to 13:
*[1,10], [2,11], [3,12], [4,13], [5], [6], [7], [8], [9]. There are 4 groups with largest size.

*Input: n = 2
*Output: 2
*Explanation: There are 2 groups [1], [2] of size 1.

*Input: n = 15
*Output: 6

*Input: n = 24
*Output: 5

!Constraints:
!1 <= n <= 10^4 """

# TODO: Approach 1: Using HashSet           [O(NxM) & O(N)] - N is size of of array, M is len of numbers


class Solution:
    def countLargestGroup(self, n: int) -> int:
        groups = {}

        for num in range(1, n+1):
            sum_ = self.digitSum(num)
            if sum_ in groups:
                groups[sum_] += 1
            else:
                groups[sum_] = 1

        largestGroups = [i for i in groups.values() if i ==
                         max(groups.values())]
        return len(largestGroups)

    def digitSum(self, num: int) -> int:
        result = 0

        while num:
            result += num % 10
            num //= 10

        return result


if __name__ == "__main__":
    n = 13  # ? Output = 4

    s = Solution()
    result = s.countLargestGroup(n)

    print("Result is {}".format(result))
