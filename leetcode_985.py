# Sum of Even Numbers After Queries
class Solution:
    def sumEvenAfterQueries(self, nums: [int], queries: [[int]]) -> [int]:
        res = []
        running_sum = sum([n for n in nums if n % 2 == 0])
        for q in queries:
            n = nums[q[1]]
            if n % 2 == 0:
                running_sum -= n
            n += q[0]
            nums[q[1]] = n
            if n % 2 == 0:
                running_sum += n
            res.append(running_sum)
        return res


s = Solution()
print(s.sumEvenAfterQueries(nums=[1, 2, 3, 4], queries=[[1, 0], [-3, 1], [-4, 0], [2, 3]]))
print(s.sumEvenAfterQueries(nums=[1], queries=[[4, 0]]))
