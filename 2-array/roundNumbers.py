# https://massivealgorithms.blogspot.com/2017/07/round-numbers-airbnb.html

from math import floor
from typing import List


class Solution:
    def roundNumbers(self, nums: List[int]):
        output = list(map(lambda x: floor(x), nums))
        remain = round(sum(nums) - sum(output))

        it = sorted(enumerate(nums), key=lambda i: i[1] - floor(i[1]))
        # it = sorted(nums, key=lambda n: n - floor(n))   # ? Output = [5, 3.3, 4]

        for _ in range(remain):
            output[it.pop()[0]] += 1

        return output


if __name__ == "__main__":
    # nums = [4.4, 3.3, 5]  # ? Output = [5, 3, 5]
    # nums = [4.4, 3.4, 5]  # ? Output = [5, 3, 5]
    nums = [1.5, 1.5, 1.1, 1.1, 1.1]  # ? Output = [1, 2, 1, 1, 1]

    s = Solution()
    result = s.roundNumbers(nums)

    print(result)
