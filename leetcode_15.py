# 3Sum
class Solution:
    def threeSum(self, nums: [int]) -> [[int]]:
        res = []
        if len(nums) < 3:
            return res
        else:
            nums.sort()
            i = 0  # -10**5 <= nums[i] <= 10**5
            while nums[i] <= 0 and i < len(nums) - 2:
                j, k = i + 1, len(nums) - 1
                while j < k:
                    if nums[i] + nums[j] + nums[k] == 0:
                        if [nums[i], nums[j], nums[k]] not in res:
                            res.append([nums[i], nums[j], nums[k]])
                        j += 1
                    elif nums[i] + nums[j] + nums[k] > 0:
                        k -= 1
                    else:
                        j += 1
                prev = nums[i]
                i += 1
            return res


s = Solution()
print(s.threeSum(nums=[-1, 0, 1, 2, -1, -4]))
print(s.threeSum(nums=[]))
print(s.threeSum(nums=[0]))
print(s.threeSum(nums=[-3, -3, 0, 1, 2, -1, -4]))
print(s.threeSum(nums=[0, 0, 0]))
print(s.threeSum(nums=[-2, 0, 1, 1, 2]))
