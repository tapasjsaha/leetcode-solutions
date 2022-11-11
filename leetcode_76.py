# Minimum Window Substring
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ls, lt = len(s), len(t)
        res, rlen = "", float('inf')
        if lt > ls:
            return res

        # create the hash table for required pattern
        need = 0
        dneed = {}
        for ch in t:
            need += 1
            if ch in dneed:
                dneed[ch] += 1
            else:
                dneed[ch] = 1

        # create the base hash table for checking
        have = 0
        dhave = {}
        for key in dneed.keys():
            dhave[key] = 0

        # Start matching the pattern
        start, end = 0, 0
        while end < ls or have == need:
            if have < need:
                # we do not have a match yet, try to get a match
                ch = s[end]
                if ch in dhave:
                    dhave[ch] += 1
                    if dhave[ch] <= dneed[ch]:
                        have += 1
                end += 1
            if have == need:
                # we have a match, try to minimize the length
                l = end - start  # not end -start + 1 as end already increased
                if l < rlen:
                    rlen = l
                    res = s[start:end]
                ch = s[start]
                if ch in dhave:
                    dhave[ch] -= 1
                    if dhave[ch] < dneed[ch]:
                        have -= 1
                start += 1
        return res


s = Solution()
print(s.minWindow(s="ADOBECODEBANC", t="ABC"))
print(s.minWindow(s="a", t="a"))
print(s.minWindow(s="a", t="aa"))
