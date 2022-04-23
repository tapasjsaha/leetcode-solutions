# Majority Element
class Solution:
    def majorityElement(self, nums: [int]) -> int:
        d = {}
        majority = len(nums) // 2
        for n in nums:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1

        for key, val in d.items():
            if val > majority:
                return key


s = Solution()
print(s.majorityElement(nums=[3, 2, 3]))
print(s.majorityElement(nums=[2, 2, 1, 1, 1, 2, 2]))
