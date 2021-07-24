# Average Salary Excluding the Minimum and Maximum Salary
class Solution:
    def average(self, salary: [int]) -> float:
        total = sum(salary) - max(salary) - min(salary)
        num = len(salary) - 2
        return total / num


s = Solution()
print(s.average(salary=[4000, 3000, 1000, 2000]))
print(s.average(salary=[1000, 2000, 3000]))
print(s.average(salary=[6000, 5000, 4000, 3000, 2000, 1000]))
print(s.average(salary=[8000, 9000, 2000, 3000, 6000, 1000]))
