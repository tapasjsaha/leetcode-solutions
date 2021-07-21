#Number of 1 Bits
class Solution:
    def hammingWeight(self, n):
        return bin(n).count('1')


s = Solution()
print(s.hammingWeight(11))