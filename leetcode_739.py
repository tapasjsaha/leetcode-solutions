# Daily Temperatures

class Solution:
    def dailyTemperatures(self, temperatures: [int]) -> [int]:
        res = [0]*len(temperatures)
        stack = []
        for i, v in enumerate(temperatures):
            if not stack:
                stack.append([v, i])
            else:
                while stack and stack[-1][0] < v:
                    res[stack[-1][1]] = i - stack[-1][1]
                    stack.pop()
                stack.append([v, i])

        return res


s = Solution()
print(s.dailyTemperatures(temperatures=[73, 74, 75, 71, 69, 72, 76, 73]))
print(s.dailyTemperatures(temperatures=[30, 40, 50, 60]))
print(s.dailyTemperatures(temperatures=[30, 60, 90]))
print(s.dailyTemperatures(temperatures=[90, 60, 30]))
print(s.dailyTemperatures(temperatures=[90]))
