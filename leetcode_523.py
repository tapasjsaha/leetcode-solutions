# Continuous Subarray Sum
class Solution:
    def checkSubarraySum(self, nums: [int], k: int) -> bool:
        # TC:O(N) SC:O(N)
        n = len(nums)
        sm = 0
        d = {0: -1}
        for i in range(n):
            sm = sm + nums[i]
            val = sm % k
            if val in d:
                if i - d[val] >= 2:
                    return True
            else:
                d[val] = i

        return False


s1 = Solution()
print(s1.checkSubarraySum(nums=[23, 2, 4, 6, 7], k=6))
print(s1.checkSubarraySum(nums=[23, 2, 6, 4, 7], k=6))
print(s1.checkSubarraySum(nums=[23, 2, 6, 4, 7], k=13))
