# Longer Contiguous Segments of Ones than Zeros
class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        cnt0, longest0 = 0, 0
        cnt1, longest1 = 0, 0
        for bit in s:
            if bit == '0':
                cnt0 += 1
                longest0 = max(longest0, cnt0)
                cnt1 = 0
            else:
                cnt0 = 0
                cnt1 += 1
                longest1 = max(longest1, cnt1)

        return longest1 > longest0


s1 = Solution()
print(s1.checkZeroOnes(s="1101"))
print(s1.checkZeroOnes(s="111000"))
print(s1.checkZeroOnes(s="110100010"))
