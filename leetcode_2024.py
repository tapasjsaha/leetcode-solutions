# Maximize the Confusion of an Exam
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def checkPossible(size):
            t = 0
            for i in range(size):
                if answerKey[i] == 'T':
                    t += 1
            if t <= k or size - t <= k:
                return True
            for i in range(size, len(answerKey), 1):
                if answerKey[i - size] == 'T':
                    t -= 1
                if answerKey[i] == 'T':
                    t += 1
                if t <= k or size - t <= k:
                    return True
            return False

        low, high = k, len(answerKey)
        ans = k
        while low <= high:
            mid = low + (high - low) // 2
            if checkPossible(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans


s = Solution()
print(s.maxConsecutiveAnswers(answerKey="TTFF", k=2))
print(s.maxConsecutiveAnswers(answerKey="TFFT", k=1))
print(s.maxConsecutiveAnswers(answerKey="TTFTTFTT", k=1))
