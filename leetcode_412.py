# Fizz Buzz
class Solution:
    def fizzBuzz(self, n: int) -> [str]:

        def helper(x: int):
            if x % 3 == 0 and x % 5 == 0:
                return "FizzBuzz"
            elif x % 3 == 0:
                return "Fizz"
            elif x % 5 == 0:
                return "Buzz"
            else:
                return str(x)

        return [helper(i) for i in range(1, n + 1, 1)]


s = Solution()
print(s.fizzBuzz(n=3))
print(s.fizzBuzz(n=5))
print(s.fizzBuzz(n=15))
