# Summary Ranges
class Solution:
    def summaryRanges(self, nums: [int]) -> [str]:
        res = []

        def helper(start, end):
            if start == end:
                res.append(str(start))
            else:
                res.append(str(start) + '->' + str(end))
            return None

        n = len(nums)
        if n != 0:
            start, end = nums[0], nums[0]
            for el in nums[1:]:
                if el == end + 1:
                    end = el
                else:
                    helper(start, end)
                    start, end = el, el
            helper(start, end)
        return res


s = Solution()
print(s.summaryRanges(nums=[0, 1, 2, 4, 5, 7]))
print(s.summaryRanges(nums=[0, 2, 3, 4, 6, 8, 9]))
print(s.summaryRanges(nums=[]))
print(s.summaryRanges(nums=[0]))
