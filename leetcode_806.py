# Number of Lines To Write String
class Solution:
    def numberOfLines(self, widths, s):
        w = {}
        for i in range(26):
            w[chr(i+97)] = widths[i]

        line = 1
        curr = 0
        for ch in s:
            if curr + w[ch] <= 100:
                curr += w[ch]
            else:
                line += 1
                curr = w[ch]

        return [line, curr]


s = Solution()
print(s.numberOfLines(
    widths=[10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
    s="abcdefghijklmnopqrstuvwxyz"))
print(s.numberOfLines(
    widths=[4, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
    s="bbbcccdddaaa"))
print(s.numberOfLines(
    widths=[4, 7, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
    s="b"))
