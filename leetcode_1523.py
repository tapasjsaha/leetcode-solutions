# Count Odd Numbers in an Interval Range
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        cnt = (high - low) // 2
        if low % 2 == 1 or high % 2 == 1:
            cnt += 1
        return cnt


s = Solution()
print(s.countOdds(low=3, high=7))
print(s.countOdds(low=8, high=10))
print(s.countOdds(low=1, high=6))
print(s.countOdds(low=2, high=7))
