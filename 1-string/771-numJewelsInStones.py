""" 771. Jewels and Stones (Easy) - Apple
https://leetcode.com/problems/jewels-and-stones/

You're given strings J representing the types of stones that are jewels, and S representing the stones you have. 
Each character in S is a type of stone you have. 
You want to know how many of the stones you have are also jewels.
The letters in J are guaranteed distinct, and all characters in J and S are letters. 
Letters are case sensitive, so "a" is considered a different type of stone from "A". """

# * Input: J = "aA", S = "aAAbbbb"
# * Output: 3

# * Input: J = "z", S = "ZZ"
# * Output: 0

#! Note:
#! S and J will consist of letters and have length at most 50.
#! The characters in J are distinct.

# TODO: Approach 1: Brute Force         [O(J.length * S.length) & O(1)]
# TODO: Approach 2: HashSet             [O(J.length + S.length) & O(1)] - O(1). Beacuse setJ has at most 26 * 2 characters ( 26 capital letters and 26 small letters).
# TODO: Approach 3: Original way        [O(J.length * S.length) & O(1)]


class Solution:
    def numJewelsInStone1(self, J: str, S: str) -> int:
        # ! Syntax meaning:
        # ? [stone in J for stone in S]
        # ? Loop through S and check if stone in J

        return sum(stone in J for stone in S)

    def numJewelsInStone2(self, J: str, S: str) -> int:
        setJ = set(J)
        return sum(stone in setJ for stone in S)

    def numJewelsInStone3(self, J: str, S: str) -> int:
        
        return sum(stone in J for stone in S)


if __name__ == "__main__":
    [J, S] = "aA", "aAAbbbb"  # ? Output = 3
    # [J, S] = "z", "ZZ"  # ? Output = 0

    s = Solution()
    result1 = s.numJewelsInStone1(J, S)
    result2 = s.numJewelsInStone2(J, S)
    result3 = s.numJewelsInStone3(J, S)

    print("Number of stones is {}".format(result1))
    print("Number of stones is {}".format(result2))
    print("Number of stones is {}".format(result3))
