# Minimum Elements to Add to Form a Given Sum
class Solution:
    def minElements(self, nums: [int], limit: int, goal: int) -> int:
        sm = sum(nums)
        goal = goal - sm
        if abs(goal) % limit == 0:
            return abs(goal) // limit
        else:
            return abs(goal) // limit + 1


s1 = Solution()
print(s1.minElements(nums=[1, -1, 1], limit=3, goal=-4))
print(s1.minElements(nums=[1, -10, 9, 1], limit=100, goal=0))
