# Array Partition
class Solution:
    def arrayPairSum(self, nums: [int]) -> int:
        # idea is to pair consecutive numbers (in terms of values)
        # TC: O(NlogN) as we have to sort, SC: O(1)
        nums.sort()
        ans = 0
        for i in range(0, len(nums), 2):
            ans += nums[i]
        return ans


s = Solution()
print(s.arrayPairSum(nums=[1, 4, 3, 2]))
print(s.arrayPairSum(nums=[6, 2, 6, 5, 1, 2]))
