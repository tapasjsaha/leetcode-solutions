# Minimum Length of String After Deleting Similar Ends
class Solution:
    def minimumLength(self, s: str) -> int:
        if len(s) == 1:
            return 1
        else:
            i, j = 0, len(s) - 1
            prefix, suffix = s[i], s[j]
            if prefix == suffix:
                while j > i and prefix == suffix:
                    if s[i] == s[i+1]:
                        i += 1
                        continue
                    if s[j] == s[j-1]:
                        j -= 1
                        continue
                    s = s[i+1:j]
                    i, j = 0, len(s) - 1
                    prefix, suffix = s[i], s[j]

                if j <= i and prefix == suffix and len(s) != 1:
                    return 0
                else:
                    return len(s)
            else:
                return len(s)



s = Solution()
print(s.minimumLength(s="bbbbbbbbbbbbbbbbbbbbbbbbbbbabbbbbbbbbbbbbbbccbcbcbccbbabbb"))
print(s.minimumLength(s="c"))
print(s.minimumLength(s="ca"))
print(s.minimumLength(s="cabaabac"))
print(s.minimumLength(s="aabccabba"))
print(s.minimumLength(s="cabaaabac"))

