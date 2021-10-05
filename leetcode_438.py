# Find All Anagrams in a String
class Solution:
    def findAnagrams(self, s: str, p: str) -> [int]:
        import string
        res = []
        if len(p) > len(s):
            return res
        else:
            ds = dict.fromkeys(string.ascii_lowercase, 0)
            dp = dict.fromkeys(string.ascii_lowercase, 0)
            for c in p:
                dp[c] += 1
            for ch in s[0:len(p)-1]:
                ds[ch] += 1
            for i in range(0, len(s)-len(p)+1, 1):
                ds[s[i + len(p) - 1]] += 1
                if ds == dp:
                    res.append(i)
                ds[s[i]] -= 1
            return res


s = Solution()
print(s.findAnagrams(s="cbaebabacd", p="abc"))
#print(s.findAnagrams(s="efgab", p="ab"))
print(s.findAnagrams(s="abab", p="ab"))
print(s.findAnagrams(s="abab", p="ac"))
print(s.findAnagrams(s="abab", p="abcde"))
