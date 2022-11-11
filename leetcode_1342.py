# Number of Steps to Reduce a Number to Zero
class Solution:
    def numberOfSteps(self, num: int) -> int:
        cnt = 0
        while num > 1:
            if num & 1 == 1:  # odd number
                num = num >> 1  # left shift i.e -1 and divide by zero
                cnt += 2
            else:  # even number
                num = num >> 1  # left shift i.e divide by zero
                cnt += 1

        if num == 1:  # for 1 it should be 1
            cnt += 1
        return cnt


s1 = Solution()
print(s1.numberOfSteps(0))
print(s1.numberOfSteps(14))
print(s1.numberOfSteps(8))
print(s1.numberOfSteps(123))

# # Solution 2
#         cnt = 0
#         while num != 0:
#             if num % 2 == 0:
#                 num = num / 2
#             else:
#                 num = num - 1
#             cnt += 1
#         return cnt

# # Solution 1
#        if num == 0:
#            return 0
#        elif num == 1:
#            return 1
#        elif num % 2 == 0:
#            return self.numberOfSteps(num / 2) + 1
#        else:
#            return self.numberOfSteps(num - 1) + 1
