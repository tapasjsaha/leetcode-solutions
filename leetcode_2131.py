# Longest Palindrome by Concatenating Two Letter Words
class Solution:
    def longestPalindrome(self, words: [str]) -> int:
        d, s = {}, set()
        count = 0

        for word in words:
            d[word] = 1 + d.get(word, 0)
            s.add(word)

        for word in s:
            if word[0] == word[1]:
                # words like aa, bb - if two such words present consider the pair
                if d[word] >= 2:
                    count += 4 * (d[word] // 2)
                    if d[word] % 2 == 0:
                        del d[word]
                    else:
                        d[word] = d[word] % 2
            else:
                # words like ab, bc - if oposite word present consider the pair
                oposite = word[1] + word[0]
                if oposite in d:
                    mn = min(d[word], d[oposite])
                    count += 4 * mn
                    del d[word]
                    del d[oposite]
                    # removed as this should not contribute any further (words which do not have oposite pair)
                else:
                    if word in d:
                        del d[word]
                    # removed as this should not contribute any further (words which do not have oposite)

        return count + 2 if d else count


s1 = Solution()
print(s1.longestPalindrome(words=["lc", "cl", "gg"]))
print(s1.longestPalindrome(words=["ab", "ty", "yt", "lc", "cl", "ab"]))
print(s1.longestPalindrome(words=["cc", "ll", "xx"]))
print(s1.longestPalindrome(words=["bb", "bb"]))
print(s1.longestPalindrome(
    words=["qo", "fo", "fq", "qf", "fo", "ff", "qq", "qf", "of", "of", "oo", "of", "of", "qf", "qf", "of"]))  # 14
