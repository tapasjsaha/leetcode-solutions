# Palindrome Number
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x == 0:
            return True
        elif x % 10 == 0:
            return False
        else:
            y = 0
            while x >= y:
                if x == y:
                    return True
                else:
                    y = (y * 10) + (x % 10)
                    if x == y:
                        return True
                    x = x // 10
        return False


s = Solution()
print(s.isPalindrome(x=1210))
print(s.isPalindrome(x=123321))
print(s.isPalindrome(x=12321))
print(s.isPalindrome(x=121))
print(s.isPalindrome(x=-121))
print(s.isPalindrome(x=12231))
print(s.isPalindrome(x=1000021))
print(s.isPalindrome(x=0))
