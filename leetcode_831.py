# Masking Personal Information
class Solution:
    def maskPII(self, s):
        if '@' in s:
            name1, rest = s.split('@')[0], s.split('@')[1]
            masked_pii = name1.lower()[0]+'*****'+name1.lower()[-1]+'@'+rest.lower()
        else:
            l = [ch for ch in s if ch in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']]
            fp = ''
            if len(l) > 10:
                for i in range (len(l) - 10):
                    fp += '*'
                fp = '+' + fp + '-'
            masked_pii = fp + '***-***-' + ''.join(l[-4:])
        return masked_pii


s = Solution()
print(s.maskPII(s="LeetCode@LeetCode.com"))
print(s.maskPII(s="AB@qq.com"))
print(s.maskPII(s="1(234)567-890"))
print(s.maskPII(s="86-(10)12345678"))
