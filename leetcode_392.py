def chkSubString(s, t):
    i = 0
    for ch in s:
        try:
            i = t.index(ch, i) + 1
        except ValueError:
            return False
    return True


def main():
    print("====================================================================")
    t = input("Enter Main String: ")
    s = input("Enter sub-string to check: ")
    x = chkSubString(s, t)

    if x:
        print(f"'{s}' is a valid substring of '{t}'")
    else:
        print(f"'{s}' is a not valid substring of '{t}'")


main()
