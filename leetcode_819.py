#Most common word:
from re import sub


def mostCommonWord(paragraph, banned):
    d = {}
    pl = sub("[!?',;.]+", " ", paragraph.lower())
    for word in pl.split(" "):
        if word in banned or word in ["", " "]:
            pass
        elif word in d.keys():
            d[word] += 1
        else:
            d[word] = 1

    k = list(d.keys())
    max_word = k[0]
    for i in k:
        if d[i] > d[max_word]:
            max_word = i
    print(d)
    return max_word


def main():
    paragraph = "Bob. hIt, baLl" # "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["bob", "hit"]  # ["hit"]
    print(mostCommonWord(paragraph, banned))


main()




