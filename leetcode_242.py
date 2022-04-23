# Valid Anagram
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        return Counter(s) == Counter(t)


s = Solution()
print(s.isAnagram(s="anagram", t="nagaram"))
print(s.isAnagram(s="rat", t="car"))

# Accepted Solution
# def isAnagram(self, s: str, t: str) -> bool:
#     ds, dt = {}, {}
#     for ch in s:
#         if ch in ds:
#             ds[ch] += 1
#         else:
#             ds[ch] = 1
#     for ch in t:
#         if ch in dt:
#             dt[ch] += 1
#         else:
#             dt[ch] = 1
#     return ds == dt
