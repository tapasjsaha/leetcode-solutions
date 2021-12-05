# Longest Common Subsequence
# https://www.youtube.com/watch?v=LAKWWDX3sGw
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1, l2 = len(text1), len(text2)
        dp = []
        for i in range(l1+1):
            temp = []
            for j in range(l2+1):
                temp.append(0)
            dp.append(temp)

        for i in range(1, l1 + 1):
            for j in range(1, l2 + 1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])

        #for i in range(l1+1):
        #    for j in range(l2+1):
        #        print(dp[i][j], end=' ')
        #    print()

        return dp[l1][l2]


s = Solution()
print(s.longestCommonSubsequence(text1="abcde", text2="ace"))
