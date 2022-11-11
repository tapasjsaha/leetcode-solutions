# Capacity To Ship Packages Within D Days
class Solution:
    def shipWithinDays(self, weights: [int], days: int) -> int:
        def daysTaken(capacity):
            nd, total = 1, 0
            for w in weights:
                if total + w <= capacity:
                    total = total + w
                else:
                    nd += 1
                    total = w
            return nd

        low, high = max(weights), sum(weights)
        ans = 0
        while low <= high:
            mid = low + (high - low) // 2
            nd = daysTaken(mid)
            if nd <= days:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans


s = Solution()
print(s.shipWithinDays(weights=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], days=5))
print(s.shipWithinDays(weights=[3, 2, 2, 4, 1, 4], days=3))
print(s.shipWithinDays(weights=[1, 2, 3, 1, 1], days=4))
