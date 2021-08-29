# Broken Calculator
class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        step = 0
        if startValue > target:
            step = startValue - target
        elif startValue < target:
            while startValue != target:
                if target == 2 * startValue:
                    step += 1
                    startValue *= 2
                elif target == (2 * startValue) - 1:
                    step += 2
                    startValue = (2 * startValue) - 1
                elif target > 2 * startValue:
                    if target % 2 == 0:
                        step += 1
                        target /= 2
                    else:
                        step += 2
                        target = (target + 1) / 2
                else:
                    step += 1
                    startValue -= 1
        else:
            pass
        return step


s = Solution()
print(s.brokenCalc(startValue=2, target=2))
print(s.brokenCalc(startValue=2, target=3))
print(s.brokenCalc(startValue=5, target=8))
print(s.brokenCalc(startValue=3, target=10))
print(s.brokenCalc(startValue=1024, target=1))

print(s.brokenCalc(startValue=6, target=40))
print(s.brokenCalc(startValue=6, target=43))
print(s.brokenCalc(startValue=6, target=41))

