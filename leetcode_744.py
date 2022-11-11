# Find Smallest Letter Greater Than Target
class Solution:
    def nextGreatestLetter(self, letters: [str], target: str) -> str:
        for ch in letters:
            if ch > target:
                return ch
        return letters[0]


s = Solution()
print(s.nextGreatestLetter(letters=["c", "f", "j"], target="a"))
print(s.nextGreatestLetter(letters=["c", "f", "j"], target="c"))
print(s.nextGreatestLetter(letters=["x", "x", "y", "y"], target="z"))
