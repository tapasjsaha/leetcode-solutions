# Own Idea - O(n2) sol
class Solution:
    def lengthOfLIS(self, nums: [int]) -> int:
        dp = [1] * len(nums)
        cnt = [1] * len(nums)
        for i in range(1, len(nums), 1):
            for j in range(i):
                if nums[j] < nums[i]:
                    if dp[i] <= dp[j]:
                        dp[i] = dp[j]+1
                        cnt[i] = cnt[j]
                    elif dp[i] == dp[j]+1:
                        cnt[i] += cnt[j]

        m = max(dp)
        res = 0
        for i in range(len(nums)):
            if dp[i] == m:
                res += cnt[i]
        return res


s = Solution()
print(s.lengthOfLIS(nums=[0, 1, 2, 3, 2, 5]))
print(s.lengthOfLIS(nums=[10, 9, 2, 5, 3, 7, 101, 18]))
print(s.lengthOfLIS(nums=[0, 1, 0, 3, 2, 3]))
print(s.lengthOfLIS(nums=[7, 7, 7, 7, 7, 7, 7]))
print(s.lengthOfLIS(nums=[1, 3, 5, 4, 7, 9, 8]))
