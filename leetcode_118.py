# Pascal's Triangle
class Solution:
    def generate(self, numRows: int) -> [[int]]:
        rowVal = [1]
        res = []
        for i in range(numRows):
            res.append(rowVal)
            temp = [0] + rowVal + [0]
            rowVal = [temp[j] + temp[j+1] for j in range(len(temp)-1)]
            rowVal = rowVal[:i+2]
        return res


s = Solution()
print(s.generate(numRows=1))
print(s.generate(numRows=5))
