# Angle Between Hands of a Clock
class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hrang = ((360 / 12) * hour) + ((360 / 720) * minutes)
        minang = (360 / 60) * minutes
        res = abs(hrang - minang)
        return min(res, 360 - res)


s = Solution()
print(s.angleClock(hour=12, minutes=30))
print(s.angleClock(hour=3, minutes=30))
print(s.angleClock(hour=3, minutes=15))
print(s.angleClock(hour=4, minutes=50))
print(s.angleClock(hour=12, minutes=0))
