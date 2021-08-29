# Add Binary
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        d = {'000': ('0', '0'), '010': ('1', '0'), '100': ('1', '0'), '110': ('0', '1'),
             '001': ('1', '0'), '011': ('0', '1'), '101': ('0', '1'), '111': ('1', '1')}
        a = a.rjust(len(b), '0')
        b = b.rjust(len(a), '0')
        res, crr = '', '0'
        for i in range(len(a)-1, -1,  -1):
            v, crr = d[a[i]+b[i]+crr]
            res = v + res

        return ('' if crr == '0' else crr) + res

# Can be done using conversion as well -> convert to int -> add -> convert to bin and return

s = Solution()
print(s.addBinary(a="11", b="1"))
print(s.addBinary(a="1010", b="1011"))
print(s.addBinary(a="10101", b="11"))
