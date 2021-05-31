# Detect Capital

def detectCapitalUse(word: str) -> bool:
    if word.isupper() or word.islower() or word[1:].islower():
        return True
    else:
        return False

#    row = word[1:]
#    if row == '' or row.islower():
#        return True
#    elif row.isupper() and word[0].isupper():
#        return True
#    else:
#        return False


def main():
    word = input("Enter word: ")
    print(detectCapitalUse(word))


main()