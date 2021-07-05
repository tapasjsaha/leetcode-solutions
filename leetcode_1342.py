#Number of Steps to Reduce a Number to Zero
class Solution:
    def numberOfSteps(self, num: int) -> int:
        cnt = 0
        while num != 0:
            if num % 2 == 0:
                num = num / 2
            else:
                num = num - 1
            cnt += 1
        return cnt


#Solution 1
#        if num == 0:
#            return 0
#        elif num == 1:
#            return 1
#        elif num % 2 == 0:
#            return self.numberOfSteps(num / 2) + 1
#        else:
#            return self.numberOfSteps(num - 1) + 1


s1 = Solution()
print(s1.numberOfSteps(0))
print(s1.numberOfSteps(14))
print(s1.numberOfSteps(8))
print(s1.numberOfSteps(123))
