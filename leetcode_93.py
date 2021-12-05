#Restore IP Addresses
class Solution:
    def restoreIpAddresses(self, s: str) -> [str]:
        res = []
        length = len(s)

        def is_valid(st):
            if len(st) < 1 or int(st) > 255:
                return False
            elif len(st) > 1 and st[0] == '0':
                return False
            else:
                return True

        def backtrack(current, remaining, start):
            if remaining == 0 and len(''.join(current[:])) == length:
                res.append('.'.join(current[:]))
            elif remaining < 0:
                return
            else:
                candidate_list = []
                for i in range(1, 4):
                    end = start + i
                    if end <= length - remaining + 1 and is_valid(s[start:end]):
                        candidate_list.append((s[start:end], end))

                for candidate in candidate_list:
                    backtrack(current+[candidate[0]], remaining-1, candidate[1])

        if len(s) < 4 or len(s) > 12:
            pass
        else:
            backtrack([], 4, 0)

        return res


s = Solution()
print(s.restoreIpAddresses(s="1234"))
print(s.restoreIpAddresses(s="25525511135"))
print(s.restoreIpAddresses(s="25525511035"))

