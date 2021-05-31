
def truncateSentence(s, k):
    lst = s.split(' ')
    o_st = ' '.join(lst[:k])
    return o_st


def main():
    in_sentence = input("Enter sentence: ")
    wtk = input("Enter number of words to be kept:")
    out_sentence = truncateSentence(in_sentence,int(wtk))

    print(f"Output sentence: {out_sentence}")


main()