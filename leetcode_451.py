# Sort Characters By Frequency
class Solution:
    def frequencySort(self, s: str) -> str:
        from collections import Counter
        d = Counter(s)
        l = sorted(list(d.items()), key=lambda x: x[1], reverse=True)
        return ''.join([x[0]*x[1] for x in l])


s = Solution()
print(s.frequencySort(s='aaabbaaAB'))
