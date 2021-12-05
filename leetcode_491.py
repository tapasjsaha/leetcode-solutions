# Increasing Subsequences
class Solution:
    def findSubsequences(self, nums: [int]) -> [[int]]:
        res = set()

        def increasing(lst):
            if len(lst) > 1:
                flag = True
                for i in range(1, len(lst)):
                    if lst[i] < lst[i - 1]:
                        flag = False
                        break
                return flag
            else:
                return False

        def backtrack(current, available):
            if len(current) > 1 and not increasing(current):
                return
            else:
                if increasing(current):
                    #res.append(current)
                    res.add(tuple(current))

                candidate_list = [(available[i], available[i + 1:]) for i in range(0, len(available))]
                for candidate in candidate_list:
                    backtrack(current+[candidate[0]], candidate[1])

        backtrack([], nums)
        return [list(r) for r in res]


s = Solution()
print(s.findSubsequences(nums=[4, 6, 7, 7]))
