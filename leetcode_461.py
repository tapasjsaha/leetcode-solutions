# Hamming Distance
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        res = x ^ y
        cnt = 0
        while res != 0:
            cnt += 1
            res = res & (res - 1)
        return cnt


s = Solution()
print(s.hammingDistance(x=1, y=4))
print(s.hammingDistance(x=3, y=1))


# # Accepted solution
# def hammingDistance(self, x: int, y: int) -> int:
#     res = x ^ y
#     cnt = 0
#     while res != 0:
#         if res & 1 == 1:
#             cnt += 1
#         res = res >> 1
#     return cnt