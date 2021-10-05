# Contains Duplicate
class Solution:
    def containsDuplicate(self, nums: [int]) -> bool:
        return len(nums) != len(set(nums))

        # Good solution but can be optimized
        # d = {}
        # for n in nums:
        #     if n in d:
        #         #d[n] += 1
        #         return True
        #     else:
        #         d[n] = 1
        # return False


s = Solution()
print(s.containsDuplicate(nums=[1, 2, 3, 1]))
print(s.containsDuplicate(nums=[1, 2, 3, 4]))
print(s.containsDuplicate(nums=[1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
print(s.containsDuplicate(nums=[1]))
print(s.containsDuplicate(nums=[0, 4, 5, 0, 3, 6]))
print(s.containsDuplicate(nums=[-1, -1, 2, 3, 1, 1]))
