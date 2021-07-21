# Longest Common Prefix
class Solution:
    def longestCommonPrefix(self, strs):
        i = 0
        while i < len(strs[0]):
            c = strs[0][i]
            for word in strs:
                try:
                    ch = word[i]
                    if c != ch:
                        return strs[0][0:i]
                except IndexError:
                    return strs[0][0:i]
            i += 1
        return strs[0][0:i]


s = Solution()
print(s.longestCommonPrefix(strs=["flower", "flow", "flight"]))
print(s.longestCommonPrefix(strs=["dog", "racecar", "car"]))
print(s.longestCommonPrefix(strs=["flo", "flower", "flow", "floight"]))
print(s.longestCommonPrefix(strs=["flower", "fl", "flow", "flight"]))

