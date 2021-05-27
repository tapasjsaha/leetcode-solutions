# Valid Parentheses

def isValid(s):
    print(s)
    stack = []
    for ch in s:
        if ch in ['(', '{', '[']:
            stack.append(ch)
        else:
            try:
                c = stack.pop()
                if c+ch == '()' or c+ch == '{}' or c+ch == '[]':
                    continue
                else:
                    return False
            except IndexError:
                return False

    if len(stack) == 0:
        return True
    else:
        return False


def main():
    s = input("Enter String: ")
    print(isValid(s))


main()