# Height Checker
class Solution:
    def heightChecker(self, heights):
        sorted_heights = sorted(heights)
        count = 0
        for i in range(len(heights)):
            if heights[i] != sorted_heights[i]:
                count += 1
        return count


s1 = Solution()

print(s1.heightChecker(heights=[1, 1, 4, 2, 1, 3]))
print(s1.heightChecker(heights=[5, 1, 2, 3, 4]))
print(s1.heightChecker(heights=[1, 2, 3, 4, 5]))
print(s1.heightChecker(heights=[5]))
