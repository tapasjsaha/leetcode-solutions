# Number Complement
class Solution:
    def findComplement(self, num: int) -> int:
        z = int('1' * len(bin(num)[2:]), 2)
        return num ^ z


s = Solution()
print(s.findComplement(num=5))
print(s.findComplement(num=1))
print(s.findComplement(num=7))
print(s.findComplement(num=10))