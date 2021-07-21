# Valid Perfect Square
class Solution:
    def isPerfectSquare(self, num):
        if num < 25:
            if num in [1, 4, 9, 16]:
                return True
            else:
                return False
        else:
            low = 1
            high = num // 4
            while low < high:
                mid = (low + high) // 2
                if mid * mid == num:
                    return True
                elif mid * mid < num:
                    if low == mid:
                        return False
                    else:
                        low = mid
                else:
                    high = mid
        return False


s = Solution()
print(s.isPerfectSquare(num=1073741824))
