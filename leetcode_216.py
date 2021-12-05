# Combination Sum III
class Solution:
    def combinationSum3(self, k: int, n: int) -> [[int]]:
        res = []

        def backtrack(current, start):
            if len(current) == k and sum(current) == n:
                res.append(current[:])
            else:
                candidate_list = [a for a in range(start, 10, 1) if a < n+1]
                for candidate in candidate_list:
                    backtrack(current+[candidate], candidate+1)

        backtrack([], 1)
        return res


s = Solution()
print(s.combinationSum3(k=3, n=7))
print(s.combinationSum3(k=1, n=7))
print(s.combinationSum3(k=3, n=9))
print(s.combinationSum3(k=4, n=1))
print(s.combinationSum3(k=3, n=2))
print(s.combinationSum3(k=9, n=45))
