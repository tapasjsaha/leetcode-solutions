# Largest Perimeter Triangle
# class Solution:
#     def largestPerimeter(self, nums: [int]) -> int:
#         perim = 0
#         nums.sort(reverse=True)
#         a, b = nums[0], nums[1]
#         for c in nums[2:]:
#             if b+c > a:
#                 perim = a+b+c
#                 break
#             else:
#                 a, b = b, c
#         return perim

class Solution:
    def largestPerimeter(self, nums: [int]) -> int:
        perim = 0
        nums.sort(reverse=True)
        a, b = nums[0], nums[1]
        for c in nums[2:]:
            if b+c > a:
                perim = a+b+c
                break
            else:
                a, b = b, c
        return perim

s = Solution()
print(s.largestPerimeter(nums=[2, 1, 2]))  # 5
print(s.largestPerimeter(nums=[1, 2, 1]))  # 0
print(s.largestPerimeter(nums=[20, 1, 21, 5, 40, 6]))  # 81
