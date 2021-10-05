# Two Sum II - Input array is sorted
class Solution:
    def twoSum(self, numbers: [int], target: int) -> [int]:
        d = {}
        for number in numbers:
            gap = target - number
            if gap in d:
                return [numbers.index(gap)+1, numbers.index(d[gap])+1]
            else:
                d[number] = gap
        return None

#    def twoSum(self, numbers: [int], target: int) -> [int]:
#        i, j = 0, len(numbers) - 1
#        while i < j:
#            if numbers[i] + numbers[j] == target:
#                return [i + 1, j + 1]
#            elif numbers[i] + numbers[j] > target:
#                j -= 1
#            else:
#                i += 1
#        return None



s = Solution()
print(s.twoSum(numbers=[2, 7, 11, 15], target=9))
print(s.twoSum(numbers=[2, 3, 4], target=6))
print(s.twoSum(numbers=[-1, 0], target=-1))
print(s.twoSum(numbers=[2, 7, 11, 15], target=18))