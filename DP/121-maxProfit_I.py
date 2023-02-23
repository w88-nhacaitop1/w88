""" 121. Best Time to Buy and Sell Stock | (Easy)
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Say you have an array for which the ith element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.
Note that you cannot sell a stock before you buy one. """

# *Input: [7,1,5,3,6,4]
# *Output: 5
# *Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# *             Not 7-1 = 6, as selling price needs to be larger than buying price.

# *Input: [7,6,4,3,1]
# *Output: 0
# *Explanation: In this case, no transaction is done, i.e. max profit = 0.

# TODO: Approach 1: Brute Force                          [O(NxN) & O(1)]
# TODO: Approach 2: One Pass - Look for minPrice         [O(N) & O(1)]
# TODO: Approach 3: Dynamic Programming

from typing import List
import sys


class Solution:
    def maxProfit(self, price: List[int]) -> int:
        INT_MAX = sys.maxsize
        # INT_MIN = -sys.maxsize

        maxProfit = 0
        minPrice = INT_MAX

        for i in range(len(prices)):
            if (prices[i] < minPrice):
                minPrice = prices[i]
            elif (prices[i] - minPrice > maxProfit):
                maxProfit = prices[i] - minPrice

        return maxProfit


if __name__ == "__main__":
    # prices = [7, 1, 5, 3, 6, 4]  # ? Output = 5
    # prices = [7, 6, 4, 3, 1]  # ? Output = 0
    prices = [1, 2]  # ? Output = 1

    s = Solution()
    print("Max Profit is {}".format(s.maxProfit(prices)))
