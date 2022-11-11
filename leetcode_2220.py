# Minimum Bit Flips to Convert Number
class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        res = start ^ goal
        cnt = 0
        while res != 0:
            if res & 1 == 1:
                cnt += 1
            res = res >> 1
        return cnt


s = Solution()
print(s.minBitFlips(start=10, goal=7))
print(s.minBitFlips(start=3, goal=4))

# # Solution 1 # Accepted
# class Solution:
#     def minBitFlips(self, start: int, goal: int) -> int:
#         res = start ^ goal
#         return bin(res).count('1')
