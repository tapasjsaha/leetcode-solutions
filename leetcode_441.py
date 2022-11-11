# Arranging Coins
class Solution:
    def arrangeCoins(self, n: int) -> int:
        low, high = 1, n
        while high-low > 1:
            mid = (high+low)//2
            req = (mid*(mid+1))//2
            if req <= n:
                low = mid
            else:
                high = mid
        return low


s = Solution()
print(s.arrangeCoins(n=5))
print(s.arrangeCoins(n=8))
print(s.arrangeCoins(n=1))
