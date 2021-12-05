# Edit Distance
# https://www.youtube.com/watch?v=XYi2-LPrwm4
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1, l2 = len(word1), len(word2)
        if l1 == 0 or l2 == 0:
            return l1+l2
        else:
            # create DP matrix
            dp = []
            for i in range(l1):
                temp = []
                for j in range(l2):
                    temp.append(0)
                temp.append(l1-i)
                dp.append(temp)
            temp = []
            for j in range(l2+1):
                temp.append(l2-j)
            dp.append(temp)

            # populate DP matrix
            for i in range(l1-1, -1, -1):
                for j in range(l2-1, -1, -1):
                    if word1[i] == word2[j]:
                        dp[i][j] = dp[i+1][j+1]
                    else:
                        dp[i][j] = min(dp[i + 1][j + 1], dp[i + 1][j], dp[i][j + 1]) + 1

            #for i in range(l1+1):
            #    for j in range(l2+1):
            #        print(dp[i][j], end=" ")
            #    print()

            return dp[0][0]


s = Solution()
print(s.minDistance(word1="", word2=""))
print(s.minDistance(word1="", word2="abc"))
print(s.minDistance(word1="abc", word2=""))

print(s.minDistance(word1="horse", word2="ros"))
print(s.minDistance(word1="intention", word2="execution"))
