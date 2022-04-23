# Arithmetic Subarrays
class Solution:
    def checkArithmeticSubarrays(self, nums: [int], l: [int], r: [int]) -> [bool]:

        def _isArithmatic(lst) -> bool:
            if len(lst) < 2:
                return False
            elif len(lst) == 2:
                return True
            else:
                diff = lst[1] - lst[0]
                i = 2
                while i < len(lst):
                    if lst[i] - lst[i - 1] != diff:
                        return False
                    i += 1
                return True

        res = []
        for i in range(len(l)):
            arr = nums[l[i]:r[i] + 1]
            res.append(_isArithmatic(sorted(arr)[:]))
        return res


s = Solution()
print(s.checkArithmeticSubarrays(nums=[4, 6, 5, 9, 3, 7], l=[0, 0, 2], r=[2, 3, 5]))
print(s.checkArithmeticSubarrays(nums=[-12, -9, -3, -12, -6, 15, 20, -25, -20, -15, -10], l=[0, 1, 6, 4, 8, 7],
                                 r=[4, 4, 9, 7, 9, 10]))
