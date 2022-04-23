# Richest Customer Wealth
class Solution:
    def maximumWealth(self, accounts: [[int]]) -> int:
        return max([sum(account) for account in accounts])



s = Solution()
print(s.maximumWealth(accounts=[[1, 2, 3], [3, 2, 1]]))
print(s.maximumWealth(accounts=[[1, 5], [7, 3], [3, 5]]))
print(s.maximumWealth(accounts=[[2, 8, 7], [7, 1, 3], [1, 9, 5]]))

# maxwealth = 0
# for account in accounts:
#     if sum(account) > maxwealth:
#         maxwealth = sum(account)
# return maxwealth