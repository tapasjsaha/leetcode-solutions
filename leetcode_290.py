# Word Pattern
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        st = s.split()
        if len(st) != len(pattern):
            return False
        else:
            d_pattern = {}
            for i in range(len(pattern)):
                if pattern[i] in d_pattern:
                    if d_pattern[pattern[i]] != st[i]:
                        return False
                else:
                    if st[i] in d_pattern.values():
                        return False
                    else:
                        d_pattern[pattern[i]] = st[i]
            return True


s = Solution()
print(s.wordPattern(pattern="abba", s="dog cat cat dog"))
print(s.wordPattern(pattern="abba", s="dog cat cat fish"))
print(s.wordPattern(pattern="aaaa", s="dog cat cat dog"))
print(s.wordPattern(pattern="abba", s="dog dog dog dog"))
print(s.wordPattern(pattern="abbac", s="dog dog dog dog"))

#can be optimized using one dict and key/value check