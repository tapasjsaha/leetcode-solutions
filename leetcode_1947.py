# Maximum Compatibility Score Sum
class Solution:
    def maxCompatibilitySum(self, students: [[int]], mentors: [[int]]) -> int:
        pop_len = len(mentors)
        ans_len = len(mentors[0])
        res = []
        d = {}

        def compatibility(s, m):
            if (s, m) in d:
                return d[(s, m)]
            else:
                com = 0
                for i in range(ans_len):
                    if students[s][i] == mentors[m][i]:
                        com += 1
                d[(s, m)] = com
                return com

        def total_compatibility(std, men):
            tot_com = 0
            for i in range(pop_len):
                tot_com += compatibility(std[i], men[i])
            return tot_com

        def backtrack(current, available):
            if not available:
                res.append(current[:])
            else:
                candidate_list = available[:]
                for candidate in candidate_list:
                    available.remove(candidate)
                    backtrack(current + [candidate], available)
                    available.append(candidate)

        backtrack([], [i for i in range(pop_len)])
        std = [i for i in range(pop_len)]
        max_com = 0
        for perm in res:
            val = total_compatibility(std, perm)
            if max_com < val:
                max_com = val

        return max_com


s = Solution()
print(s.maxCompatibilitySum(students=[[1, 1, 0], [1, 0, 1], [0, 0, 1]], mentors=[[1, 0, 0], [0, 0, 1], [1, 1, 0]]))
print(s.maxCompatibilitySum(students=[[0, 0], [0, 0], [0, 0]], mentors=[[1, 1], [1, 1], [1, 1]]))
