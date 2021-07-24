# Text Justification
class Solution:
    def fullJustify(self, words: list, maxWidth: int) -> list:
        res, curr_list, curr_width = [], [], maxWidth
        for word in words:
            if len(word) <= curr_width:
                curr_list.append(word)
                curr_width -= (len(word) + 1)
            else:
                res.append(curr_list)
                curr_list = [word]
                curr_width = maxWidth - len(word) -1
        res.append(curr_list)

        curr_list = res[:]
        res = []
        for ls in curr_list[:-1]:
            gap = len(ls) - 1
            remain_len = maxWidth - sum([len(word) for word in ls])
            #print(ls, gap, remain_len)
            if gap != 0:
                normal_pad = remain_len // gap
                extra_pad = remain_len - (normal_pad * gap)
            else:
                normal_pad, extra_pad = remain_len, 0
            #print(normal_pad, extra_pad)
            s = ''
            for word in ls:
                if extra_pad > 0:
                    s = s + word + (' ' * normal_pad) + ' '
                    extra_pad -= 1
                else:
                    s = s + word + (' ' * normal_pad)
            res.append(s)

        s = ''
        for word in curr_list[-1]:
            s = s + word + ' '
        s = s + (' ' * maxWidth)
        res.append(s)

        return [item[:maxWidth] for item in res]


s = Solution()
print(s.fullJustify(words=["This", "is", "an", "example", "of", "text", "justification."], maxWidth=16))
print(s.fullJustify(words=["What", "must", "be", "acknowledgment", "shall", "be"], maxWidth=16))
print(s.fullJustify(
    words=["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to", "a", "computer.",
           "Art", "is", "everything", "else", "we", "do"], maxWidth=20))
