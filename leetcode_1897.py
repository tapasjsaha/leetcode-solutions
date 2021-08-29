# Redistribute Characters to Make All Strings Equal
class Solution:
    def makeEqual(self, words: [str]) -> bool:
        from collections import Counter
        n = len(words)
        d = Counter(''.join(words))
        for v in d.values():
            x = v / n
            if not x.is_integer():
                return False
        return True


s = Solution()
print(s.makeEqual(words=["abc", "aabc", "bc"]))
print(s.makeEqual(words=["ab", "a"]))
