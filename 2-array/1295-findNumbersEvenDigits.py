""" 1295. Find Numbers with Even Number of Digits (Easy)
https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

Given an array nums of integers, return how many of them contain an even number of digits.
 
*Input: nums = [12,345,2,6,7896]
*Output: 2
*Explanation: 
    12 contains 2 digits (even number of digits). 
    345 contains 3 digits (odd number of digits). 
    2 contains 1 digit (odd number of digits). 
    6 contains 1 digit (odd number of digits). 
    7896 contains 4 digits (even number of digits). 
    Therefore only 12 and 7896 contain an even number of digits.

*Input: nums = [555,901,482,1771]
*Output: 1 
*Explanation: 
    Only 1771 contains an even number of digits.
 
!Constraints:
!1 <= nums.length <= 500
!1 <= nums[i] <= 10^5
"""

# TODO: Approach 1: Using Log10 check           [O(N) & O(1)]
# TODO: Approach 2: Convert to string           [O(N) & O(1)]

from typing import List
import math


class Solution:
    def findNumbers1(self, nums: List[int]) -> int:
        count = 0
        # for num in nums:
        #     if num >= 10 and int(math.log10(num)) % 2 == 0:
        #         count += 1

        # return count

        return sum([1 for n in nums if int(math.log10(n)) % 2 == 1])

    def findNumbers2(self, nums: List[int]) -> int:
        return sum([1 for n in nums if len(str(n)) % 2 == 0])


if __name__ == "__main__":
    nums = [12, 345, 2, 6, 7896]
    # nums = [95135,5325,86961,29024,56957,8582,38050,18348,22076,66080,32572,34641,13247,22750,34933,1,43104,69600,13753,2928,91003,66897,35461,71034,21168,8362,41429,4986,28778,54065,92406,89609,53352,27528,92404,83934,22730,13608,58946,31091,55473,42031,88547,39821,8581,8448,80212,9895,46849,60819,76670,65404,54013,93755,33697,32283,54709,7601,41638,47793,55555,30786,74127,55797,41596,55097,51550,51256,79974,2096,40960,45341,91887,33025,38747,72510,56027,59759,20730,60539,59981,75486,18959,23893,85701,21555,36012,98669,65510,15810,28645,96656,28925,72297,23650,39636,55599,35422,96798,57174,7920,33801,49068,94663,59829,33156,6,79563,26760,80624,57056,25,52487,47784,75029,73643,32964,91717,50668,48615,17023,79894,65618,38698,35519,72398,67989,41813,97388,50186,27563,96154,33924,33546,45214,50586,89568,80843,91114,89367,22473,65941,29293,49781,77524,13020,51849,4228,62323,65886,63020,72342,73395,21486,82153,58449,45959,36851,72029,19729,8312,92227,12115,66902,93834,35869,29269,39884,11419,7937,78676,8126,92189,85158,18264,58898,236,45863,43955,21529,37843,25509,90364,68124,16148,94664,25224,10172,39582,42169,72984,42287,66869,67497,13777,2481,37835,80900,90991,90412,8758,95701,73952,43243,37684,79295,73568,69501,55476,71429,66956,52668,95862,78891,1351,87524,81589,87674,45525,41842,5443,41445,97993,35898,51449,79639,73374,28561,11923,52118,21105,92249,74417,2448,51098,66196,75592,4807,31219,5919,2314,77587,75582,61816,39627,23488,316,77220,58469,84940,82362,6201,23849,11145,27567,25435,28382,24811,80439,60605,84322,43306,60222,92122,38129,99758,5963,78172,80689,49450,22541,62577,87357,62913,37835,59383,56206,40587,39346,87742,4167,14587,42081,38116,14437,31826]
    # nums = [100]
    # nums = [9999]

    s = Solution()
    result1 = s.findNumbers1(nums)
    result2 = s.findNumbers2(nums)

    print("[Approach 1] Count is {}".format(result1))
    print("[Approach 2] Count is {}".format(result2))
