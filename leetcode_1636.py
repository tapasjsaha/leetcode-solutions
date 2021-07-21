# Sort Array by Increasing Frequency
class Solution:
    def frequencySort(self, nums):
        d = {}
        for n in nums:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1
        nums.sort(key=lambda x: (d[x], -x))
        return nums


s = Solution()
print(s.frequencySort(nums=[1, 1, 2, 2, 2, 3]))
print(s.frequencySort(nums=[2, 3, 1, 3, 2]))
print(s.frequencySort(nums=[-1, 1, -6, 4, 5, -6, 1, 4, 1]))
