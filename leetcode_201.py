# Bitwise AND of Numbers Range
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        res = left & right
        if res == 0:
            return res
        else:
            # print("I am here")
            interval = right - left
            res = list(bin(res)[2:])
            res.reverse()
            for i in range(len(res)):
                if res[i] == '1' and 2**i <= interval:
                    res[i] = '0'
            res.reverse()
            return int(''.join(res), 2)


s = Solution()
print(s.rangeBitwiseAnd(left=5, right=7))
print(s.rangeBitwiseAnd(left=0, right=0))
print(s.rangeBitwiseAnd(left=10, right=11))
print(s.rangeBitwiseAnd(left=1, right=292829))
