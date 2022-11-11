# Construct the Rectangle
class Solution:
    def constructRectangle(self, area: int) -> [int]:
        n = 1
        while n * n <= area:
            if area % n == 0:
                W = n
                L = area // n
            n += 1
        return [L, W]


s = Solution()
print(s.constructRectangle(area=4))
print(s.constructRectangle(area=37))
print(s.constructRectangle(area=122122))
