# Can Place Flowers
class Solution:
    def canPlaceFlowers(self, flowerbed: [int], n: int) -> bool:
        flowerbed = [0]+flowerbed+[0]
        i = 1
        if n == 0:
            return True
        else:
            while i < len(flowerbed)-1 and n > 0:
                if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                    flowerbed[i] = 1
                    n -= 1
                i += 1
                if n == 0:
                    return True
        return False


s = Solution()
print(s.canPlaceFlowers(flowerbed=[1, 0, 0, 0, 1], n=1))
print(s.canPlaceFlowers(flowerbed=[1, 0, 0, 0, 1], n=2))
print(s.canPlaceFlowers(flowerbed=[0], n=1))
print(s.canPlaceFlowers(flowerbed=[0, 1], n=1))
print(s.canPlaceFlowers(flowerbed=[0, 1], n=0))
print(s.canPlaceFlowers(flowerbed=[0, 0], n=1))
