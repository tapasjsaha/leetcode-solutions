# Additive Number
class Solution:
    def isAdditiveNumber(self, num: str) -> bool:

        def backtrack(n1, n2, st, found):
            if st == '' and found:
                return True
            elif st == '' and not found:
                return False
            else:
                l = len(str(n1+n2))
                if int(st[:l]) == n1+n2:
                    return backtrack(n2, int(st[:l]), st[l:], True)
                else:
                    return False
                
        if len(num) < 3:
            return False
        else:
            for i in range(1, len(num)-1, 1):
                # print(num[:i])
                if num[:i] == str(int(num[:i])):
                    for j in range(i+1, len(num), 1):
                        # print(num[i:j], num[j:])
                        if num[i:j] == str(int(num[i:j])):
                            vaild = backtrack(int(num[:i]), int(num[i:j]), num[j:], False)
                            if vaild:
                                return True
            return False


s = Solution()
print(s.isAdditiveNumber("123"))
print(s.isAdditiveNumber("112358"))
print(s.isAdditiveNumber("112359"))
print(s.isAdditiveNumber("199910001999"))
print(s.isAdditiveNumber("112233"))