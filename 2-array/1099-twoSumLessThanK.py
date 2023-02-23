""" 
* 1099. Two Sum Less Than K
* https://leetcode.com/problems/two-sum-less-than-k/

* Given an array A of integers and integer K, return the maximum S such that there exists i < j with A[i] + A[j] = S and S < K.
* If no i, j exist satisfying this equation, return -1.

* Input: A = [34,23,1,24,75,33,54,8], K = 60
* Output: 58
* Explanation:
* We can use 34 and 24 to sum 58 which is less than 60.
* Example 2:

* Input: A = [10,20,30], K = 15
* Output: -1
* Explanation:
* In this case it's not possible to get a pair sum less that 15.

* Note:
* 1 <= A.length <= 100
* 1 <= A[i] <= 1000
* 1 <= K <= 2000

TODO: Approach 1: Using Two Pointers  [O(N) & O(1)] 

"""

from typing import List


class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        A.sort()

        left = 0
        right = len(A)-1
        closestToK = -1

        while left < right:
            currentSum = A[left] + A[right]
            if(currentSum < K):
                left += 1
                closestToK = max(currentSum, closestToK)
            else:
                right -= 1
                
        return closestToK


if __name__ == "__main__":
    A = [34, 23, 1, 24, 75, 33, 54, 8]
    K = 60

    s = Solution()
    print(s.twoSumLessThanK(A, K))