# Repeated DNA Sequences
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> [str]:

        # Rabin Karp Algorithm
        def rollingHash(value, old, new):
            return ((value - (old * 4**9)) * 4) + new

        result_dict = {}
        ACGT = {'A': 1, 'C': 2, 'G': 3, 'T': 4}         # base is 4 as only 4 elements are present
        total, hashkey = 0, 0
        if len(s) <= 10:
            return []
        else:
            i, j = 0, 10
            strng = s[i:j]
            for indx, ch in enumerate(strng):
                hashkey += ACGT[ch] * (4 ** (j - indx - 1))
            result_dict[(hashkey, strng)] = 1

            while j < len(s):
                strng = s[i+1:j+1]
                hashkey = rollingHash(hashkey, ACGT[s[i]], ACGT[s[j]])
                if (hashkey, strng) in result_dict:
                    result_dict[(hashkey, strng)] += 1
                else:
                    result_dict[(hashkey, strng)] = 1
                i += 1
                j += 1
            print(result_dict)
            return [k[1] for k, v in result_dict.items() if v > 1]


s = Solution()
print(s.findRepeatedDnaSequences("AAAA"))
print(s.findRepeatedDnaSequences("AAAAAAAAAAAA"))
print(s.findRepeatedDnaSequences("AAAAAATCGAAAAA"))
print(s.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))