#Count and Say
class Solution:
    def countAndSay(self, n: int) -> str:
        if n-1 == 0:
            return self.cas_str('0')
        else:
            return self.cas_str(self.countAndSay(n-1))

    @staticmethod
    def cas_str(inp):
        res = ""
        st = list(inp)
        cnt = 1
        prev = st.pop(0)
        if inp == '0':
            res = '1'
        elif len(st) == 0:
            res = str(cnt) + prev
        else:
            while len(st) > 0:
                curr = st.pop(0)
                if curr == prev:
                    cnt += 1
                else:
                    res = res + str(cnt) + prev
                    prev = curr
                    cnt = 1
            res = res + str(cnt) + prev
        return res


s1 = Solution()
print(s1.countAndSay(4))
