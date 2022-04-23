# Subarray Sum Equals K
# https://www.youtube.com/watch?v=fFVZt-6sgyo
class Solution:
    def subarraySum(self, nums: [int], k: int) -> int:
        prefix_sum, count = 0, 0
        d = {0: 1}
        for n in nums:
            prefix_sum += n
            sum_val = prefix_sum - k
            if sum_val in d:
                count += d[sum_val]
            if prefix_sum in d:
                d[prefix_sum] += 1
            else:
                d[prefix_sum] = 1

        return count


s = Solution()
print(s.subarraySum(nums=[-1, -1, 1], k=0))
print(s.subarraySum(nums=[1, 1, 1], k=2))
print(s.subarraySum(nums=[1, 2, 3], k=3))
print(s.subarraySum(nums=[3, 1, 2, 3], k=3))
print(s.subarraySum(nums=[1, -1, 1, 1, 1, 1], k=3))
