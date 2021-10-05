# Best Time to Buy and Sell Stock

# Algo - 10**5 (inf) is my initial buy price, calculate profit array for each day,
# if profit is -ve consider it zero, lowest price so far should be new buy price

class Solution:
    def maxProfit(self, prices: [int]) -> int:
        buy_price = 100000
        profits = []
        for price in prices:
            profits.append(max(0, price-buy_price))
            buy_price = min(buy_price, price)
        return max(profits)


s = Solution()
print(s.maxProfit(prices=[7, 1, 5, 3, 6, 4]))
print(s.maxProfit(prices=[7, 6, 4, 3, 1]))
