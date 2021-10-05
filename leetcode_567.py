# Permutation in String
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        import string
        s1_len, s2_len = len(s1), len(s2)
        if s1_len > s2_len or not set(s1).issubset(set(s2)):
            return False

        ds1 = dict.fromkeys(string.ascii_lowercase, 0)  # create a dictionary with all alphabate count 0
        ds2 = dict.fromkeys(string.ascii_lowercase, 0)  # create a dictionary with all alphabate count 0

        for c in s1:
            ds1[c] += 1

        i, j = 0, s1_len
        for c in s2[i:j]:
            ds2[c] += 1

#       print(ds1)
        while j <= s2_len:
#           print(ds2)
            if ds1 == ds2:
                return True
            else:
                ds2[s2[i]] -= 1
                i += 1
                if j < s2_len:
                    ds2[s2[j]] += 1
                j += 1
        return False


s = Solution()
print(s.checkInclusion(s1="adc", s2="dcda"))
print(s.checkInclusion(s1="abcd", s2="ei"))
print(s.checkInclusion(s1="abc", s2="eidbaooo"))
print(s.checkInclusion(s1="ab", s2="eidbaooo"))
print(s.checkInclusion(s1="ab", s2="eidboaoo"))
