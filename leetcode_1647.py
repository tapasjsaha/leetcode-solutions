# Minimum Deletions to Make Character Frequencies Unique
class Solution:
    def minDeletions(self, s: str) -> int:
#        cnt, d = 0, {}
#        for c in s:
#            if c in d:
#                d[c] += 1
#            else:
#                d[c] = 1
#        lst = [v for k, v in d.items()]

        cnt = 0
        lst = [s.count(ch) for ch in set(s)]
        lst.sort(reverse=True)
        for i in range(1, len(lst), 1):
            if lst[i] >= lst[i - 1]:
                rf = (lst[i] - lst[i - 1]) + 1
                if lst[i] - rf >= 0:
                    lst[i] = lst[i] - rf
                    cnt += rf
                else:
                    cnt += lst[i]
                    lst[i] = 0
        return cnt


s = Solution()
print(s.minDeletions(s="aab"))
print(s.minDeletions(s="aaabbbcc"))
print(s.minDeletions(s="ceabaacb"))

print(s.minDeletions(s="eefaaaaabbbbbcccdggggghhhhhh"))
