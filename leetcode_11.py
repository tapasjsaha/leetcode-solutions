# Container With Most Water
class Solution:
    def maxArea(self, height: [int]) -> int:
        i, j = 0, len(height) - 1
        res = 0
        while i < j:
            hgth, wdth = min(height[i], height[j]), j - i
            area = hgth * wdth
            if area > res:
                res = area

            # Modify the minimum height
            if height[i] < height[j]:
                i += 1
            elif height[i] > height[j]:
                j -= 1
            else:
                if height[i + 1] > height[j - 1]:
                    i += 1
                else:
                    j -= 1
        return res


s = Solution()
print(s.maxArea(height=[1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(s.maxArea(height=[1, 8, 6, 100, 100, 4, 8, 3, 7]))
print(s.maxArea(height=[4, 3, 2, 1, 4]))
print(s.maxArea(height=[1, 2, 1]))
