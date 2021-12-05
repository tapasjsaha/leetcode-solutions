# Arithmetic Slices
class Solution:
    def numberOfArithmeticSlices(self, nums: [int]) -> int:
        def numberofsubstr(lst):
            if len(lst) < 3:
                return 0
            else:
                dp = [0] * len(lst)
                for i in range(3, len(lst) + 1, 1):
                    dp[i - 1] = len(lst) - i + 1
                # print(dp)
                return sum(dp)

        slices = []
        def createAP(lst):
            if len(lst) < 3:
                pass
            else:
                temp = [lst[0], lst[1]]
                for i in range(2, len(lst), 1):
                    if lst[i-1] - lst[i-2] == lst[i] - lst[i-1]:
                        temp.append(lst[i])
                    else:
                        slices.append(temp[:])
                        createAP(lst[i-1:])
                        break
                if i == len(lst)-1:
                    slices.append(temp)

        if len(nums) < 3:
            pass
        else:
            createAP(nums)
        print(slices)
        total = 0
        for slice in slices:
            total += numberofsubstr(slice)
        return total


s = Solution()
#print(s.numberOfArithmeticSlices(nums=[1]))
print(s.numberOfArithmeticSlices(nums=[1, 2, 3]))
print(s.numberOfArithmeticSlices(nums=[1, 2, 3, 4]))
print(s.numberOfArithmeticSlices(nums=[1, 3, 5, 7, 9]))

print(s.numberOfArithmeticSlices(nums=[1, 2, 3, 8, 9, 10]))
print(s.numberOfArithmeticSlices(nums=[1, 2, 3, 5, 7, 8, 9, 15, 20, 25]))
