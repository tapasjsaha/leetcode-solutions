# First Unique Character in a String

def firstUniqChar(s):
    d = {}
    ind = -1
    for ch in s:
        if ch in d:
            d[ch] += 1
        else:
            d[ch] = 1
    for ch in s:
        if d[ch] == 1:
            ind = s.index(ch)
            break
    return ind

def main():
    s = input("Enter string: ")
    print(firstUniqChar(s))


main()