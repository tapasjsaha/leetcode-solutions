# Isomorphic Strings
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        ds = {}
        dt = {}
        if len(s) != len(t):
            return False
        else:
            for i in range(len(s)):
                chs = s[i]
                cht = t[i]
                if chs not in ds and cht not in dt:
                    ds[chs] = cht
                    dt[cht] = chs
                elif chs in ds and cht in dt:
                    if ds[chs] == cht and dt[cht] == chs:
                        continue
                    else:
                        return False
                else:
                    return False
            return True

s1 = Solution()

print(s1.isIsomorphic(s="egg", t="add"))
print(s1.isIsomorphic(s="foo", t="bar"))
print(s1.isIsomorphic(s="paper", t="title"))
print(s1.isIsomorphic(s="a", t="b"))
print(s1.isIsomorphic(s="a", t="a"))
print(s1.isIsomorphic(s="aa", t="ab"))
