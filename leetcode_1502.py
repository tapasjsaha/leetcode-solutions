# Can Make Arithmetic Progression From Sequence
class Solution:
    def canMakeArithmeticProgression(self, arr):
        if len(arr) == 2:
            return True
        else:
            arr.sort()
            for i in range(len(arr) - 2):
                if arr[i + 1] - arr[i] == arr[i + 2] - arr[i + 1]:
                    continue
                else:
                    return False
            return True


s1 = Solution()

print(s1.canMakeArithmeticProgression(arr=[3, 5, 1]))
print(s1.canMakeArithmeticProgression(arr=[1, 2, 4]))
print(s1.canMakeArithmeticProgression(arr=[1, 2, 4, 6, 8]))
print(s1.canMakeArithmeticProgression(arr=[10, 2, 4, 8, 6]))
