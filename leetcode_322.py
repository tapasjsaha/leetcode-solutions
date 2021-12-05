# Coin Change
# https://www.youtube.com/watch?v=H9bfqozjoqs
class Solution:
    def coinChange(self, coins: [int], amount: int) -> int:
        valid_coins = set()
        for coin in coins:
            if coin <= amount:
                valid_coins.add(coin)
        coins = list(valid_coins)
        coins.sort()

        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount+1):
            for coin in coins:
                if a-coin >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - coin])

        return dp[amount] if dp[amount] != amount+1 else -1


s = Solution()
print(s.coinChange(coins=[1, 2, 5], amount=11))
print(s.coinChange(coins=[1, 2, 5], amount=0))
print(s.coinChange(coins=[1, 2, 5, 5, 5, 5, 5, 5, 5, 5], amount=13))
print(s.coinChange(coins=[9, 8, 5], amount=1))
print(s.coinChange(coins=[3, 7, 405, 436], amount=8839))
print(s.coinChange(coins=[3, 7, 5, 6], amount=11))

# TLE
