# Delete Operation for Two Strings
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1, l2 = len(word1), len(word2)
        #if l1 == 0 or l2 == 0:
        #    return l1 + l2
        # Not required as length >= 1

        dp = []
        for i in range(l1+1):
            temp = []
            for j in range(l2+1):
                temp.append(0)
            dp.append(temp)

        for i in range(1, l1 + 1):
            for j in range(1, l2 + 1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])

        #for i in range(l1+1):
        #    for j in range(l2+1):
        #        print(dp[i][j], end=' ')
        #    print()

        return (l1 + l2) - (2 * dp[l1][l2])


s = Solution()
print(s.minDistance(word1="abcde", word2="ace"))
