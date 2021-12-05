# Pascal's Triangle II
class Solution:
    def getRow(self, rowIndex: int) -> [int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        else:
            prev = self.getRow(rowIndex - 1)
            res = [1]+[prev[i]+prev[i+1] for i in range(len(prev)-1)]+[1]
            return res


s = Solution()
print(s.getRow(rowIndex=10))

# Valid solution but TLE
# class Solution:
#     def getRow(self, rowIndex: int) -> [int]:
#         res = [0] * (rowIndex + 1)
#
#         def helper(row, col):
#             if col == 0 or row == col:
#                 return 1
#             else:
#                 return helper(row-1, col-1) + helper(row-1, col)
#
#         for colIndex in range((len(res)//2)+1):
#             res[colIndex] = helper(rowIndex, colIndex)
#
#         i, j = 0, len(res)-1
#         while i < j:
#             res[j] = res[i]
#             i += 1
#             j -= 1
#
#         return res