# Maximum Product Difference Between Two Pairs
class Solution:
    def maxProductDifference(self, nums: [int]) -> int:
        # O(N) Solution
        min1, min2, max2, max1 = 100001, 100001, 0, 0
        for n in nums:
            if n < min2:
                if n < min1:
                    min2 = min1
                    min1 = n
                else:
                    min2 = n

            if n > max2:
                if n > max1:
                    max2 = max1
                    max1 = n
                else:
                    max2 = n

        return (max1 * max2) - (min1 * min2)


# O(NlogN) solution which will work without TLE
# nums.sort()
# min1,min2,max2,max1 = nums[0], nums[1], nums[-2], nums[-1]
# return (max1*max2) - (min1*min2)

s = Solution()
print(s.maxProductDifference(nums=[5, 6, 2, 7, 4]))
print(s.maxProductDifference(nums=[4, 2, 5, 9, 7, 4, 8]))
