# Koko Eating Bananas
class Solution:
    def minEatingSpeed(self, piles: [int], h: int) -> int:
        def hours(total, rate):
            if total % rate == 0:
                return total // rate
            else:
                total = total + (rate - (total % rate))
                return total // rate

        def totalHours(rate):
            total = 0
            for p in piles:
                total += hours(p, rate)
            return total

        low, high = 1, max(piles)
        ans = 1
        while low <= high:
            mid = (low + high) // 2
            time = totalHours(mid)
            if time <= h:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans


s = Solution()
print(s.minEatingSpeed(piles=[3, 6, 7, 11], h=8))
print(s.minEatingSpeed(piles=[30, 11, 23, 4, 20], h=5))
print(s.minEatingSpeed(piles=[30, 11, 23, 4, 20], h=6))
