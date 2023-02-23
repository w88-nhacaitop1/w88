
# TODO: Approach 1: Using Two Pointers

from typing import List


class Solution:
    def hasPairWithSum(self, arr: List[int], S: int) -> bool:
        ans = False
        left = 0
        right = len(arr) - 1

        while left < right:
            _sum = arr[left] + arr[right]
            if _sum == S:
                return True
            elif _sum < S:
                left += 1
            else:
                right -= 1

        return ans


if __name__ == "__main__":
    arr = [1, 2, 3, 9]
    # arr = [1, 2, 4, 4]
    S = 8

    s = Solution()
    print(s.hasPairWithSum(arr, S))
