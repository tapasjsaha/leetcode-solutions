# How Many Numbers Are Smaller Than the Current Number
class Solution:
    def smallerNumbersThanCurrent(self, nums: [int]) -> [int]:
        d = {}
        temp = nums[:]
        temp.sort(reverse=True)
        temp.append(-1)
        for ind, val in enumerate(temp[:-1]):
            if val == temp[ind + 1]:
                continue
            else:
                d[val] = len(temp[ind:]) - 2
        temp = []
        for v in nums:
            temp.append(d[v])
        return temp


s = Solution()
print(s.smallerNumbersThanCurrent(nums=[8, 1, 2, 2, 3]))
print(s.smallerNumbersThanCurrent(nums=[6, 5, 4, 8]))
print(s.smallerNumbersThanCurrent(nums=[7, 7, 7, 7]))
print(s.smallerNumbersThanCurrent(nums=[0, 0]))
