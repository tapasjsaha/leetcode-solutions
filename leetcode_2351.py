# First Letter to Appear Twice
class Solution:
    def repeatedCharacter(self, s: str) -> str:
        st = set()
        for ch in s:
            if ch in st:
                return ch
            else:
                st.add(ch)


s = Solution()
print(s.repeatedCharacter(s="abccbaacz"))
print(s.repeatedCharacter(s="abcdd"))
print(s.repeatedCharacter(s="aa"))
