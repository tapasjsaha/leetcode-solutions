# Number of Different Integers in a String
class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        # TC : O(N), SC: O(N)
        st = ""
        for ch in word:
            if ch.isdigit():
                st = st + ch
            else:
                st = st + ' '
        lst = st.split(' ')

        s = set()
        for l in lst:
            if l.isdecimal():
                s.add(int(l))

        return len(s)


s = Solution()
print(s.numDifferentIntegers(word="a123bc34d8ef34"))
print(s.numDifferentIntegers(word="leet1234code234"))
print(s.numDifferentIntegers(word="a1b01c001"))
