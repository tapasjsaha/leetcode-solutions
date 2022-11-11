# Decode String
class Solution:
    def decodeString(self, s: str) -> str:
        if s == "":
            return ""
        elif s[0].isalpha():
            st = self.decodeString(s[1:])
            return s[0] + st
        else:
            dig = s[0]
            counter, start = 0, 1
            # k can be more than 1 digit, hence find the start by '['
            while s[start] != '[':
                dig += s[start]
                start += 1

            for i in range(start + 1, len(s)):
                if s[i] == ']' and counter == 0:
                    break
                elif s[i] == ']':
                    counter -= 1
                elif s[i] == '[':
                    counter += 1
                else:
                    pass
            st1 = self.decodeString(s[start + 1:i])
            st2 = self.decodeString(s[i + 1:])
            return (int(dig) * st1) + st2


s1 = Solution()
print(s1.decodeString(s="3[a]2[bc]"))
print(s1.decodeString(s="3[a2[c]]"))
print(s1.decodeString(s="2[abc]3[cd]ef"))
print(s1.decodeString(s="21[abc]32[cd]ef"))
