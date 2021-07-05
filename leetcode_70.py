#Climbing Stairs
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            prev = 1
            curr = 2
            for i in range(n-2):
                prev, curr = curr, prev + curr
            return curr

# TIME LIMIT EXCEEDED
#       if n == 1:
#           return 1
#       elif n == 2:
#           return 2
#       else:
#           return self.climbStairs(n - 1) + self.climbStairs(n - 2)

s1 = Solution()

print(s1.climbStairs(1))
print(s1.climbStairs(2))
print(s1.climbStairs(3))
print(s1.climbStairs(4))
print(s1.climbStairs(5))
print(s1.climbStairs(35))
print(s1.climbStairs(50))