# Gray Code
# Recursive Solution: check for n-1 bit sol. add 0 before the list and the 1 before the reverse list
class Solution:
    def grayCode(self, n: int) -> [int]:

        def greyCodeRecur(n):
            if n == 1:
                res = ['0', '1']
            else:
                res = []
                temp = greyCodeRecur(n-1)
                for val in temp:
                    res.append('0'+val)
                for val in temp[::-1]:
                    res.append('1'+val)
            return res

        return [int(x, 2) for x in greyCodeRecur(n)]


s = Solution()
print(s.grayCode(16))


# Not working for high values of N
# def grayCode(self, n: int) -> [int]:
#     res = []
#
#     def bit_count(x):
#         count = 0
#         while x:
#             count += x & 1
#             x >>= 1
#         return count
#
#     def backtrack(current, available):
#         if len(current) == 2 ** n and not available:
#             if bit_count(0 ^ current[-1]) == 1:
#                 res.append(current)
#         else:
#             candidate_list = [num for num in available if bit_count(num ^ current[-1]) == 1]
#             for candidate in candidate_list:
#                 available.remove(candidate)
#                 backtrack(current + [candidate], available[:])
#                 available.append(candidate)
#                 if res:
#                     return
#
#     available = [i for i in range(1, 2 ** n)]
#     backtrack([0], available)
#     return res