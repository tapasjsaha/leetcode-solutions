# Single Number
class Solution:
    def singleNumber(self, nums: [int]) -> int:
        res = (2 * sum(set(nums))) - sum(nums)
        return res

        #res = [n for n in set(nums) if nums.count(n) == 1]
        #return res[0]




    # Below solution works as xor of any number with itself always returns zero
    #    ans = 0
    #    n = len(nums)
    #    for i in range(n):
    #        ans ^= nums[i]
    #    return ans





s = Solution()
print(s.singleNumber(nums=[2, 2, 1]))
print(s.singleNumber(nums=[4, 1, 2, 1, 2]))
print(s.singleNumber(nums=[1]))
