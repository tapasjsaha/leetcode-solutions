# Maximum Points You Can Obtain from Cards
class Solution:
    def maxScore(self, cardPoints: [int], k: int) -> int:
        n = len(cardPoints)
        precp = [cardPoints[0]]
        sufcp = [cardPoints[-1]]
        for i in range(1, k, 1):
            precp.append(cardPoints[i] + precp[i - 1])
            sufcp.append(cardPoints[n - i - 1] + sufcp[i - 1])

        print(precp, sufcp)
        mscore = 0
        for i in range(k + 1):
            score = 0 if i == 0 else precp[i - 1]
            score = score + (0 if i == k else sufcp[k - i - 1])
            mscore = max(mscore, score)

        return mscore


s = Solution()
print(s.maxScore(cardPoints=[1, 2, 3, 4, 5, 6, 1], k=3))
print(s.maxScore(cardPoints=[2, 2, 2], k=2))
print(s.maxScore(cardPoints=[9, 7, 7, 9, 7, 7, 9], k=7))
print(s.maxScore(cardPoints=[1, 2, 100, 4, 5, 6, 1], k=3))

print(s.maxScore(cardPoints=[100, 40, 17, 9, 73, 75], k=3))
