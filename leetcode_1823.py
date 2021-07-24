# Find the Winner of the Circular Game
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friend = list(range(1, n+1, 1))
        i = 0
        while len(friend) > 1:
            j = (i + k - 1) % n
            friend.pop(j)
            i = j
            n -= 1

        return friend[0]


s = Solution()
print(s.findTheWinner(n=5, k=2))
print(s.findTheWinner(n=6, k=5))
print(s.findTheWinner(n=1, k=5))
