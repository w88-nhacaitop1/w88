""" Amazon Logistics would like to quickly set up a roof over a parking lot. 
There are many cars parked in the parking lot and the lot is in a straight line. There are n cars currently
parked and a roofer needs to cover them with a roof . The requirement is that at least k cars currently in the lot are covered
by the roof. Determine the minimum length of the roof to cover k cars.

Example:
  n = 4
  cars = [6,2,12,7]
  k = 3

Two roofs that cover three cars are possible: one covering spots 2 through 7 with a length of 6, and another covering
slots 6 through 12 with a length of 7. The shortest roof that meets the requirement is of length 6.
"""

from typing import List
import math

class Solution:
    def carParkingRoof(self, n: int, cars: List[int], k: int):
        result, j = math.inf, 0

        cars.sort()

        for i in range(n):
            j = i + k - 1;

            if j < n:
                result = min(result, cars[j] - cars[i] + 1)

        return 0 if result == math.inf else result


if __name__ == "__main__":
    # n, cars, k = 4, [6, 2, 12, 7], 3    #? Output = 6
    # n, cars, k = 4, [2, 10, 8, 17], 3   #? Output = 9
    n, cars, k = 4, [1, 2, 3, 10], 4      #? Output = 10

    s = Solution()
    result1 = s.carParkingRoof(n, cars, k)

    print("Result 1: {0}".format(result1))
    