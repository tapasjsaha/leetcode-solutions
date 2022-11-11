# Teemo Attacking
class Solution:
    def findPoisonedDuration(self, timeSeries: [int], duration: int) -> int:
        if len(timeSeries) == 1:
            return duration
        else:
            res = 0
            prev = timeSeries[0]
            for curr in timeSeries[1:]:
                if curr - prev > duration:
                    res += duration
                else:
                    res += curr - prev
                prev = curr
            return res + duration


s = Solution()
print(s.findPoisonedDuration(timeSeries=[1, 4], duration=2))
print(s.findPoisonedDuration(timeSeries=[1, 2], duration=2))
