# Split a String Into the Max Number of Unique Substrings
class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        global maxlen
        maxlen = 0

        def backtrack(current, available):
            if not available:
                if maxlen < len(current):
                    globals()['maxlen'] = len(current)
                    # print(current)
            elif len(current) + len(available) < maxlen:
                return
            else:
                candidate_list = [available[0:i] for i in range(1, len(available)+1)]
                for candidate in candidate_list:
                    if candidate not in current:
                        current.add(candidate)
                        backtrack(current, available[available.index(candidate) + len(candidate):])
                        current.remove(candidate)
                    else:
                        continue

        backtrack(set(), s)
        return maxlen


s = Solution()
print(s.maxUniqueSplit(s="ababccc"))
print(s.maxUniqueSplit(s="aba"))
print(s.maxUniqueSplit(s="aa"))
print(s.maxUniqueSplit(s="a"))
print(s.maxUniqueSplit(s="bbbb"))
print(s.maxUniqueSplit(s="wwwzfvedwfvhsww"))

