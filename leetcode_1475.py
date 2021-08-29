# Final Prices With a Special Discount in a Shop
class Solution:
    def finalPrices(self, prices: [int]) -> [int]:
        res = []
        for i, price in enumerate(prices):
            for j in range (i+1, len(prices), 1):
                if prices[j] <= price:
                    res.append(price - prices[j])
                    break
            else:
                res.append(price)
        return res


s = Solution()
print(s.finalPrices(prices=[8, 4, 6, 2, 3]))
print(s.finalPrices(prices=[1, 2, 3, 4, 5]))
print(s.finalPrices(prices=[10, 1, 1, 6]))
