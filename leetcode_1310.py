# XOR Queries of a Subarray
class Solution:
    def xorQueries(self, arr: [int], queries: [[int]]) -> [int]:
        # for p length arr and q queries TC:O(p+q), SC:O(p)
        # Constructing prefix xor array
        pfx, curr = [], 0
        for a in arr:
            curr = curr ^ a
            pfx.append(curr)

        # Answering queries
        res = []
        for q in queries:
            if q[0] == 0:
                ans = pfx[q[1]]
            else:
                ans = pfx[q[1]] ^ pfx[q[0] - 1]
            res.append(ans)

        return res


s1 = Solution()
print(s1.xorQueries(arr=[1, 3, 4, 8], queries=[[0, 1], [1, 2], [0, 3], [3, 3]]))
print(s1.xorQueries(arr=[4, 8, 2, 10], queries=[[2, 3], [1, 3], [0, 0], [0, 3]]))
