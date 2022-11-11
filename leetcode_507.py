# Perfect Number
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False
        else:
            res = [1]
            n = 2
            while n * n <= num:
                if num % n == 0:
                    if num // n == n:
                        res.append(n)
                    else:
                        res.extend([n, num // n])
                n += 1
        return sum(res) == num


s = Solution()
print(s.checkPerfectNumber(num=28))
print(s.checkPerfectNumber(num=7))
