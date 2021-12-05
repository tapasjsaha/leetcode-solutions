# Happy Number
class Solution:
    def isHappy(self, n: int) -> bool:
        d = {}
        for i in range(10):
            d[i] = i * i
        x = set()
        while n not in x:
            x.add(n)
            temp = 0
            while n > 0:
                temp += d[n % 10]
                n = n // 10
            if temp == 1:
                return True
            else:
                n = temp
            # print(n)
        return False


s = Solution()
print(s.isHappy(19))
print(s.isHappy(2))
