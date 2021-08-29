# Remove K Digits
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        lst = [int(i) for i in num]
        i, ln = 0, len(lst)-1
        while i < ln and k > 0:
            if lst[i] > lst[i+1]:
                lst.pop(i)
                ln -= 1
                i = -1   #bad design to start the loop again
                k -= 1
            i += 1
        if k == 0:
            pass
        elif sum(lst) == 0:
            pass
        elif all(lst[i] <= lst[i+1] for i in range(len(lst)-1)):
            while lst and k > 0:
                lst.remove(max(lst))
                k -= 1
        if lst:
            ch = [str(c) for c in lst]
        else:
            ch = ['0']
        return str(int(''.join(ch)))


s = Solution()
print(s.removeKdigits(num="112", k=1))
print(s.removeKdigits(num="9", k=1))
print(s.removeKdigits(num="1432219", k=3))
print(s.removeKdigits(num="10200", k=1))
print(s.removeKdigits(num="10", k=2))
print(s.removeKdigits(num="1234", k=1))
print(s.removeKdigits(num="4123", k=2))
print(s.removeKdigits(num="3421", k=2))
print(s.removeKdigits(num="1342", k=2))
print(s.removeKdigits(num="2413", k=2))
