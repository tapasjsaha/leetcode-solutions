# Maximum Number of Balloons
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        d = {}
        for ch in text:
            d[ch] = 1 + d.get(ch, 0)

        res = min(d.get('b', 0), d.get('a', 0), d.get('l', 0) // 2, d.get('o', 0) // 2, d.get('n', 0))
        return res


s1 = Solution()
print(s1.maxNumberOfBalloons(text="nlaebolko"))
print(s1.maxNumberOfBalloons(text="loonbalxballpoon"))
print(s1.maxNumberOfBalloons(text="leetcode"))
