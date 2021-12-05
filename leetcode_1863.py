# Sum of All Subset XOR Totals
class Solution:
    def subsetXORSum(self, nums: [int]) -> int:
        res = []

        def xor(inp_lst):
            lst = [a for a in inp_lst if a]
            if not lst:
                return 0
            else:
                ans = lst[0]
                for val in lst[1:]:
                    ans = ans ^ val
                return ans

        def backtrack(current, available):
            if not available:
                res.append(current[:])
            else:
                candidate_list = [None, available[0]]
                for candidate in candidate_list:
                    backtrack(current + [candidate], available[1:])

        backtrack([], nums)

        xors = [xor(lst) for lst in res]
        return sum(xors)


s = Solution()
print(s.subsetXORSum(nums=[1, 3]))
print(s.subsetXORSum(nums=[5, 1, 6]))
print(s.subsetXORSum(nums=[3, 4, 5, 6, 7, 8]))
