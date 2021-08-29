# Decrypt String from Alphabet to Integer Mapping
class Solution:
    def freqAlphabets(self, s: str) -> str:
        d = {"1": "a", "2": "b", "3": "c", "4": "d", "5": "e", "6": "f", "7": "g", "8": "h", "9": "i", "10": "j",
             "11": "k", "12": "l", "13": "m", "14": "n", "15": "o", "16": "p", "17": "q", "18": "r", "19": "s",
             "20": "t", "21": "u", "22": "v", "23": "w", "24": "x", "25": "y", "26": "z"}
        lst = list(s)
        res = ""
        while lst:
            ch = lst.pop()
            if ch == '#':
                x = lst.pop()
                y = lst.pop()
                res = d[y+x] + res
            else:
                res = d[ch] + res
        return res


s = Solution()
print(s.freqAlphabets(s="10#11#12"))
print(s.freqAlphabets(s="1326#"))
print(s.freqAlphabets(s="25#"))
print(s.freqAlphabets(s="12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"))
