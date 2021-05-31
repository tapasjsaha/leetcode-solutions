# Ransom Note

def canConstruct(ransomNote: str, magazine: str) -> bool:
    for ch in set(ransomNote):
        if ransomNote.count(ch) > magazine.count(ch):
            return False
    return True

    # print(ransomNote,magazine)
#    lm = list(magazine)
#    for ch in ransomNote:
#        try:
#            lm.remove(ch)
#        except ValueError:
#            return False
#    return True


def main():
    rn = input("Enter ransom note: ")
    mz = input("Enter magazine: ")
    print(canConstruct(rn,mz))


main()


