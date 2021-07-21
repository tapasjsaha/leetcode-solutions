#Check if the Sentence Is Pangram
class Solution:
    def checkIfPangram(self, sentence):
        #s = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}
        return set(sentence) == {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}


#        test = [0] * 26
#        for ch in set(sentence):
#            test[ord(ch)-97] = 1
#        return sum(test) == 26


s = Solution()
print(s.checkIfPangram(sentence = "thequickbrownfoxjumpsoverthelazydog"))
print(s.checkIfPangram(sentence = "leetcode"))
print(s.checkIfPangram(sentence = "abcdefghijklmnopqrstuvwxyz"))
print(s.checkIfPangram(sentence = "bcdefghijklmnopqrstuvwxyz"))