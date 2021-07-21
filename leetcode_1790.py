# Check if One String Swap Can Make Strings Equal
class Solution:
    def areAlmostEqual(self, s1, s2):
        l = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                l.append(i)
        if len(l) == 0:
            return True
        elif len(l) == 2:
            i = l[0]
            j = l[1]
            #s = s2[:i] + s2[j] + s2[i + 1:j] + s2[i] + s2[j + 1:]
            #return s == s1
            return s1[i] == s2[j] and s1[j] == s2[i]
        else:
            return False


s = Solution()
print(s.areAlmostEqual(s1="bank", s2="kanb"))
print(s.areAlmostEqual(s1="attack", s2="defend"))
print(s.areAlmostEqual(s1="kelb", s2="kelb"))
print(s.areAlmostEqual(s1="abcd", s2="dcba"))
