# Sort Array By Parity II
class Solution:
    def sortArrayByParityII(self, nums):
        res = [1] * len(nums)
        e = 0
        o = 1
        for n in nums:
            if n % 2 == 0:
                res[e] *= n
                e += 2
            else:
                res[o] *= n
                o += 2
        return res


s1 = Solution()
print(s1.sortArrayByParityII(nums=[4, 2, 5, 7]))
print(s1.sortArrayByParityII(nums=[2, 3]))
print(s1.sortArrayByParityII(nums=[4, 2, 5, 7, 0, 3, 1, 6]))
