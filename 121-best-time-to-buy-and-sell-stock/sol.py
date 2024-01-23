from ast import List

#Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max = 0
        currBuy = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < currBuy:
                currBuy = prices[i]
            elif prices[i] - currBuy > max:
                max = prices[i] - currBuy

        return max
