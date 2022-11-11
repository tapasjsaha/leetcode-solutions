# Maximum 69 Number
class Solution:
    def maximum69Number (self, num: int) -> int:
        # The idea is to change the MSB possible from 6 to 9
        # For a given N number of digits is logN base 10 hence TC=O(logN base 10), SC = O(1)
        Flag = 1
        ans = 0
        power = len(str(num))-1
        while num:
            dig = num // (10**power)
            num = num % (10**power)
            power -= 1
            if Flag > 0 and dig == 6:
                dig = 9
                Flag -= 1
            ans = ans * 10 + dig
        return ans

# class Solution:
# For a given N number of digits is logN base 10 hence TC=O(logN base 10), SC = O(logN base 10)
#     def maximum69Number(self, num: int) -> int:
#         l = list(str(num))
#         if l.count('6') == 0:
#             return num
#         else:
#             ind = l.index('6')
#             l[ind] = '9'
#         return int(''.join(l))


s = Solution()
print(s.maximum69Number(num=9669))
print(s.maximum69Number(num=9996))
print(s.maximum69Number(num=9999))
print(s.maximum69Number(num=9))
print(s.maximum69Number(num=6))
