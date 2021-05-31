def toLowerCase(s):
    res = ''
    for ch in s:
        if 65 <= ord(ch) <= 90:
            res += chr(ord(ch) + 32)
        else:
            res += ch
    return res


def main():
    in_str = input("Enter string: ")
    out_str = toLowerCase(in_str)
    print(f"Output String: {out_str}")


main()