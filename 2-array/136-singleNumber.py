""" 136. Single Number (Easy)
https://leetcode.com/problems/single-number/

Given a non-empty array of integers, every element appears twice except for one. Find that single one.

!Note:
!Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

* Input: [2,2,1]
* Output: 1

* Input: [4,1,2,1,2]
* Output: 4 """

# TODO: Approach 1: List Operation                      [O(N*N) & O(N)] - Using List
# TODO: Approach 2: Hash Table                          [O(N) & O(1)] - Using dict()
# TODO: Approach 3: Math 2∗(a+b+c)−(a+a+b+b+c)=c        [O(N) & O(1)] - Using HashSet
# TODO: Approach 4: Bit Manipulation (XOR)              [O(N) & O(1)] - Best solution & satisfy the requirement

from typing import List


class Solution:
    def singleNumber3(self, nums: List[int]) -> int:
        return 2 * sum(set(nums)) - sum(nums)

    def singleNumber4(self, nums: List[int]) -> int:
        result = 0

        for num in nums:
            result ^= num

        return result


if __name__ == "__main__":
    # nums = [2, 2, 1] # ? Ouput = 1
    nums = [4, 1, 2, 1, 2]  # ? Ouput = 4

    s = Solution()
    result3 = s.singleNumber3(nums)
    result4 = s.singleNumber4(nums)

    print("[Approach 3] Result is {}".format(result3))
    print("[Approach 4] Result is {}".format(result4))
