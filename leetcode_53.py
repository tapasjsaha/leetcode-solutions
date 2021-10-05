# Maximum Subarray
class Solution:
    def maxSubArray(self, nums: [int]) -> int:
        # # Kadane's Algorithm
        # max_so_far = nums[0]
        # sum_so_far = 0
        # for i, v in enumerate(nums):
        #     sum_so_far += v
        #     max_so_far = max(max_so_far, sum_so_far)
        #     sum_so_far = max(sum_so_far, 0)
        # return max_so_far

        # Follow up : Divide and Conquer
        def maxCrossingSum(nums, l, m, h):
            # Sum of left part
            sum = 0
            left_sum = -99999999
            for i in range(m, l-1, -1):
                sum += nums[i]
                left_sum = max(sum, left_sum)
            # Sum of right part
            sum = 0
            right_sum = -99999999
            for i in range(m+1, h+1, 1):
                sum += nums[i]
                right_sum = max(sum, right_sum)
            # return
            return max(left_sum, right_sum, left_sum+right_sum)

        l, h = 0, len(nums)-1
        if l == h:
            return nums[l]
        else:
            m = (l+h)//2
            msa = max(self.maxSubArray(nums[l:m+1]), self.maxSubArray(nums[m+1:h+1]), maxCrossingSum(nums, l, m, h))
            return msa




s = Solution()
print(s.maxSubArray(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(s.maxSubArray(nums=[1]))
print(s.maxSubArray(nums=[-2]))
print(s.maxSubArray(nums=[5, 4, -1, 7, 8]))
