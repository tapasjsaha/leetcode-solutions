# Group Anagrams
class Solution:
    def groupAnagrams(self, strs: [str]) -> [[str]]:
        d = {}
        for s in strs:
            key = ''.join(sorted(s))
            if key in d:
                d[key].append(s)
            else:
                d[key] = [s]

        res = [val for val in d.values()]
        return res
    

s = Solution()
print(s.groupAnagrams(strs=["abc", "bca", "cab"]))
print(s.groupAnagrams(strs=["", "", ""]))
print(s.groupAnagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"]))


# Accepted solution but only 5%
# import string
#
# str_list, res = [], []
# for s in strs:
#     d = dict.fromkeys(string.ascii_lowercase, 0)
#     for ch in s:
#         d[ch] += 1
#     str_list.append((s, d))
#
# while str_list:
#     s, d = str_list.pop(0)
#     new_group = [s]
#     to_be_deleted = []
#     for st, dt in str_list:
#         if d == dt:
#             new_group.append(st)
#             to_be_deleted.append((st, dt))
#     for x in to_be_deleted:
#         str_list.remove(x)
#     res.append(new_group)
# return res
