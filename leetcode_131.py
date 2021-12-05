# Palindrome Partitioning
class Solution:
    def partition(self, s: str) -> [[str]]:
        res = []

        def backtrack(current, available):
            if len(available) == 0:
                res.append(current[:])
            else:
                # Construct candidate
                candidate_list = []
                for i in range(1, len(available)+1, 1):
                    if available[:i] == available[:i][::-1]:
                        candidate_list.append(available[:i])
                # main loop
                for candidate in candidate_list:
                    backtrack(current+[candidate], available[len(candidate):])

        backtrack([], s)
        return res


s = Solution()
print(s.partition(s="aab"))
print(s.partition(s="a"))
print(s.partition(s="acabaca"))
