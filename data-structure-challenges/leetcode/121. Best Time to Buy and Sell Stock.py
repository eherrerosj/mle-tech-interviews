"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a
different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction.
If you cannot achieve any profit, return 0.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

Constraints:
    1 <= prices.length <= 105
    0 <= prices[i] <= 104

Learnings:
- Another possible solution: find local min and search for local max, use sliding windows
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = None
        maxprofit = 0
        for price in prices:
            if minprice is None or minprice > price:
                minprice = price
            elif price - minprice > maxprofit:
                maxprofit = price - minprice
        return maxprofit


# sol = Solution().maxProfit([7, 1, 5, 3, 6, 4])
# print(sol == 5)


# sol = Solution().maxProfit([1, 1, 5, 3, 2, 4])
# print(sol == 4)

# sol = Solution().maxProfit([7, 6, 5, 4, 4, 5])
# print(sol == 1)

# sol = Solution().maxProfit([1])
# print(sol == 0)

# sol = Solution().maxProfit([10, 10, 10])
# print(sol == 0)

sol = Solution().maxProfit([2, 1, 2, 1, 0, 1, 2])
print(sol == 2)
