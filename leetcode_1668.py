# Maximum Repeating Substring
class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        low, high = 0, len(sequence)
        res = 0
        while low <= high:
            mid = low + (high - low) // 2
            ch = mid * word
            if ch in sequence:
                res = mid
                low = mid + 1
            else:
                high = mid - 1
        return res


s = Solution()
print(s.maxRepeating(sequence="ababc", word="ab"))
print(s.maxRepeating(sequence="ababc", word="ba"))
print(s.maxRepeating(sequence="ababc", word="ac"))
