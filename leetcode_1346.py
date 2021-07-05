# Check If N and Its Double Exist

class Solution:
    def checkIfExist(self, arr):
        d = {arr[0]: arr[0]}
        for a in arr[1:]:
            if a * 2 in d:
                return True
            elif a % 2 == 0 and int(a / 2) in d:
                return True
            else:
                d[a] = a
        return False


s1 = Solution()
print(s1.checkIfExist([10, 2, 5, 3]))
print(s1.checkIfExist([7, 1, 14, 11]))
print(s1.checkIfExist([3, 1, 7, 11]))
