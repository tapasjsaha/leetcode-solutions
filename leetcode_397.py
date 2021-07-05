# Integer Replacement
class Solution:
    def integerReplacement(self, n: int) -> int:
        count = 0
        if n == 1:
            return 0
        else:
            while n != 1:
                if n % 2 == 0:
                    n /= 2
                elif (n + 1) % 4 == 0 and n != 3:
                    n += 1
                else:
                    n -= 1
                count += 1
        return count


# Recursive solution but not good in terms of runtime
#        if n == 1:
#            return 0
#        elif n % 2 == 0:
#            return 1 + self.integerReplacement(n // 2)
#        else:
#            return 1 + min(self.integerReplacement(n + 1), self.integerReplacement(n - 1))


s1 = Solution()

print(s1.integerReplacement(n=8))
print(s1.integerReplacement(n=7))
print(s1.integerReplacement(n=4))
print(s1.integerReplacement(n=41))
print(s1.integerReplacement(n=43))

