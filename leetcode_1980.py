# Find Unique Binary String
class Solution:
    def findDifferentBinaryString(self, nums: [str]) -> str:
        n = len(nums[0])
        global finished, res
        finished = False
        res = None

        def backtrack(current, n):
            if len(current) == n and ''.join(current) not in nums:
                globals()['finished'] = True
                globals()['res'] = ''.join(current)
            elif len(current) == n:
                return
            else:
                candidate_list = ['0', '1']
                for candidate in candidate_list:
                    backtrack(current+[candidate], n)
                    if globals()['finished']:
                        return

        backtrack([], n)
        return res


s = Solution()
print(s.findDifferentBinaryString(nums=["11", "10", "00"]))


# def findDifferentBinaryString(self, nums: [str]) -> str:
#     n = len(nums[0])
#     global finished, res
#     finished = False
#     res = None
#
#     def backtrack(current, n):
#         if len(current) == n and ''.join(current) not in nums:
#             globals()['finished'] = True
#             globals()['res'] = ''.join(current)
#         elif len(current) == n:
#             return
#         else:
#             candidate_list = ['0', '1']
#             for candidate in candidate_list:
#                 backtrack(current + [candidate], n)
#                 if globals()['finished']:
#                     return
#
#     backtrack([], n)
#     return res
