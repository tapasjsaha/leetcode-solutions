# Check if Word Equals Summation of Two Words
class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        d = {'a': '0', 'b': '1', 'c': '2', 'd': '3', 'e': '4', 'f': '5', 'g': '6', 'h': '7', 'i': '8', 'j': '9'}
        fn = ''.join([d[c] for c in firstWord])
        sn = ''.join([d[c] for c in secondWord])
        tn = ''.join([d[c] for c in targetWord])
        return int(fn) + int(sn) == int(tn)


s = Solution()
print(s.isSumEqual(firstWord="acb", secondWord="cba", targetWord="cdb"))
print(s.isSumEqual(firstWord="aaa", secondWord="a", targetWord="aab"))
print(s.isSumEqual(firstWord="aaa", secondWord="a", targetWord="aaaa"))
