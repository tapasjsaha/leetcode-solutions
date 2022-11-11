# Max Consecutive Ones III
class Solution:
    def longestOnes(self, nums: [int], k: int) -> int:
        def check(n):
            sm = sum(nums[:n])
            if sm + k >= n:
                return True
            else:
                for i in range(n, len(nums), 1):
                    sm = sm + nums[i] - nums[i - n]
                    if sm + k >= n:
                        return True
                return False

        low, high = 0, len(nums)
        ans = 0
        while low <= high:
            mid = low + (high - low) // 2
            if check(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans


s1 = Solution()
print(s1.longestOnes(nums=[1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], k=2))
print(s1.longestOnes(nums=[0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], k=3))
