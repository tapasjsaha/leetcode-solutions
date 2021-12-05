# https://www.youtube.com/watch?v=cjWnW0hdF1Y
# Own Idea - O(n2) sol
class Solution:
    def lengthOfLIS(self, nums: [int]) -> int:
        dp = [1] * len(nums)
        for i in range(1, len(nums), 1):
            temp = [0]
            for j in range(i):
                if nums[j] < nums[i]:
                    temp.append(dp[j])
            dp[i] = max(temp) + 1
        return max(dp)


s = Solution()
print(s.lengthOfLIS(nums=[0, 1, 2, 3, 2, 5]))
print(s.lengthOfLIS(nums=[10, 9, 2, 5, 3, 7, 101, 18]))
print(s.lengthOfLIS(nums=[0, 1, 0, 3, 2, 3]))
print(s.lengthOfLIS(nums=[7, 7, 7, 7, 7, 7, 7]))

