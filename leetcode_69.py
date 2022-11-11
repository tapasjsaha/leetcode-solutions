# Sqrt(x)
class Solution:
    def mySqrt(self, x: int) -> int:
        low, high = 0, x
        while low < high:
            mid = (low + high) // 2
            if mid * mid > x:
                high = mid - 1
            elif mid * mid < x:
                low = mid + 1
            elif mid * mid == x:
                return mid
        return low-1 if low * low > x else low


s = Solution()
print(s.mySqrt(x=0))
print(s.mySqrt(x=1))
print(s.mySqrt(x=4))
print(s.mySqrt(x=8))
print(s.mySqrt(x=9))
print(s.mySqrt(x=15))
print(s.mySqrt(x=25))