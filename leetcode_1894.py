# Find the Student that Will Replace the Chalk
class Solution:
    def chalkReplacer(self, chalk: [int], k: int) -> int:
        k = k % sum(chalk)
        for i, c in enumerate(chalk):
            if c > k:
                return i
            else:
                k -= c


s = Solution()
print(s.chalkReplacer(chalk=[5, 1, 5], k=22))  # 0
print(s.chalkReplacer(chalk=[3, 4, 1, 2], k=25))  # 1
