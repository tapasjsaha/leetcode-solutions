def lengthOfLongestSubstring(s):
    if len(s) < 2:
        max_st = s
    else:
        i = 0
        max_st = s[i]
        while i < len(s):
            st = ""
            for ch in s[i:]:
                if ch in st:
                    if len(st) > len(max_st):
                        max_st = st
                    break
                else:
                    st += ch
                if len(st) == len(s[i:]):
                    if len(st) > len(max_st):
                        max_st = st
                    i = len(s)
            i += 1
    print(max_st)
    return len(max_st)

def main():
    s = "abcabcdjasjnckjnajsiojiosaijaosjncjnbb" #"aud" #"" #"a" #"pwwkew" #"bbbbb" #"abcabcbb"
    print(lengthOfLongestSubstring(s))


main()

#Not done yet