# Remove One Element to Make the Array Strictly Increasing
class Solution:
    def isIncreasing(self, nums):
        for i in range(len(nums)-1):
            if nums[i] >= nums[i + 1]:
                return False
        return True

    def canBeIncreasing(self, nums):
        pre = nums[:]
        post = nums[:]
        for i in range(len(nums)-1):
            if nums[i] >= nums[i + 1]:
                pre.pop(i)
                post.pop(i+1)
                print(pre, post)
                return self.isIncreasing(pre) or self.isIncreasing(post)
        return True


s = Solution()
print(s.canBeIncreasing(nums=[1, 2, 10, 5, 7]))
print(s.canBeIncreasing(nums=[1, 2, 10, 5, 11]))
print(s.canBeIncreasing(nums=[2, 3, 1, 2]))
print(s.canBeIncreasing(nums=[1, 1, 1]))
print(s.canBeIncreasing(nums=[1, 2, 3]))
print(s.canBeIncreasing(nums=[2, 1]))
print(s.canBeIncreasing(nums=[1, 2]))
