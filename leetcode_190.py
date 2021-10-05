# Reverse Bits
class Solution:
    def reverseBits(self, n: int) -> int:
        # print('{:032b}'.format(n))
        res = 0
        musk = 1
        for i in range(32):
            res = res << 1
            temp = n & musk
            res = res | temp
            n = n >> 1
        # print('{:032b}'.format(res))
        return res


s = Solution()
print(s.reverseBits(n=43261596))
