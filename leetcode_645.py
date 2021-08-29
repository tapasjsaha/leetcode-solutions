# Set Mismatch --- tle
class Solution:
    def findErrorNums(self, nums: [int]) -> [int]:
        actual_sum = int(len(nums) * (len(nums)+1) / 2)
        current_sum = sum(nums)
        set_sum = sum(set(nums))
        return [current_sum - set_sum, actual_sum - set_sum]


s = Solution()
print(s.findErrorNums(nums=[1, 2, 2, 4]))
print(s.findErrorNums(nums=[1, 1]))
print(s.findErrorNums(nums=[2, 2]))

# Correct but not in time limit
#    def findErrorNums(self, nums: [int]) -> [int]:
#        found = 0
#        for ch in range(1, len(nums)+1):
#            if nums.count(ch) == 2:
#                x = ch
#                found += 1
#            if ch not in nums:
#                y = ch
#                found += 1
#            if found == 2:
#                break
#        return [x, y]



