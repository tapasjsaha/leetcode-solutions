# Maximum Length of a Concatenated String with Unique Characters
class Solution:
    def maxLength(self, arr: [str]) -> int:
        self.largest = 0

        def backtrack(current, available):
            if not available:
                if len(current) == len(set(current)):
                    self.largest = max(self.largest, len(current))
            else:
                new = available[0]
                backtrack(current, available[1:])
                current = current + new
                if len(current) == len(set(current)):
                    backtrack(current, available[1:])

        backtrack("", arr)
        return self.largest


s = Solution()
print(s.maxLength(arr=["un", "iq", "ue"]))
print(s.maxLength(arr=["cha", "r", "act", "ers"]))
print(s.maxLength(arr=["abcdefghijklmnopqrstuvwxyz"]))
