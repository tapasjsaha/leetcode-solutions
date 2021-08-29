# Ugly Number
class Solution:
    def isUgly(self, n: int) -> bool:
        if n > 0:
            while True:
                if n % 5 == 0:
                    n /= 5
                    continue
                elif n % 3 == 0:
                    n /= 3
                    continue
                elif n % 2 == 0:
                    n /= 2
                    continue
                else:
                    break
#            if n == 1:
#                return True
#            else:
#                return False
            return n == 1  # Pythonic way of writing above 4 lines
        else:
            return False



s = Solution()
print(s.isUgly(6))
print(s.isUgly(8))
print(s.isUgly(14))
print(s.isUgly(1))
print(s.isUgly(0))
print(s.isUgly(-1))
