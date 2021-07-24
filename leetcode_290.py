# Word Pattern
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        st = s.split()
        if len(st) != len(pattern):
            return False
        else:
            d_pattern, dst = {}, {}
            for i in range(len(pattern)):
                if pattern[i] not in d_pattern:
                    if st[i] not in dst:
                        d_pattern[pattern[i]] = st[i]
                        dst[st[i]] = pattern[i]
                    else:
                        return False
                else:
                    if d_pattern[pattern[i]] == st[i] and dst[st[i]] == pattern[i]:
                        continue
                    else:
                        return False
            return True


s = Solution()
print(s.wordPattern(pattern="abba", s="dog cat cat dog"))
print(s.wordPattern(pattern="abba", s="dog cat cat fish"))
print(s.wordPattern(pattern="aaaa", s="dog cat cat dog"))
print(s.wordPattern(pattern="abba", s="dog dog dog dog"))
print(s.wordPattern(pattern="abbac", s="dog dog dog dog"))

#can be optimized using one dict and key/value check