""" 
905. Sort Array By Parity (Easy)
https://leetcode.com/problems/sort-array-by-parity/

Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.
You may return any answer array that satisfies this condition.

*Input: [3,1,2,4]
*Output: [2,4,3,1]
*The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
 
!Note:
!1 <= A.length <= 5000
!0 <= A[i] <= 5000 """

# TODO: Approach 1: Using Two pointers          [O(N) & O(1)]
# TODO: Approach 2: One Pass                    [O(N) & O(1)]
# TODO: Approach 3: Using sorted() with lambda  [O(NlogN) & O(1)]

from typing import List


class Solution:
    def sortArrayByParity1(self, A: List[int]) -> List[int]:
        i, j = 0, len(A) - 1

        while i < j:
            if A[j] % 2:
                j -= 1
            elif A[i] % 2:
                A[i], A[j] = A[j], A[i]

                i += 1
                j -= 1
            else:
                i += 1

        return A

    def sortArrayByParity2(self, A: List[int]) -> List[int]:
        even = -1

        for i in range(len(A)):
            if A[i] % 2 == 0:
                A[i], A[even+1] = A[even+1], A[i]
                even += 1

        return A

    def sortArrayByParity3(self, A: List[int]) -> List[int]:
        """ It sorts the values in the list on the basis of the logic of the lambda function
        *In the test case input is [3,1,2,4] : 
        *Lambda Function will iterate each value and return 0[False] or 1[True] on the basis of even or odd
        *Lambda will give value for the input [3,1,2,4] : [1,1,0,0] and by default is sorts in ascending order
        *It will become [0,0,1,1] """

        return sorted(A, key=lambda i: i % 2 != 0)


if __name__ == "__main__":
    # nums = [0]  # ? Output = [0]
    # nums = [1]  # ? Output = [1]
    # nums = [0, 1]  # ? Output = [0, 1]
    # nums = [0, 2]  # ? Output = [0, 2]
    # nums = [3, 0, 1]  # ? Output = [0, 3, 1]
    nums = [3, 1, 2, 4]  # ? Output = [4, 2, 1, 3]
    # nums = [3, 0, 1, 1]  # ? Output = [0, 3, 1, 1]

    s = Solution()
    result1 = s.sortArrayByParity1(nums)
    result2 = s.sortArrayByParity2(nums)
    result3 = s.sortArrayByParity3(nums)

    print(result1)
    print(result2)
    print(result3)
