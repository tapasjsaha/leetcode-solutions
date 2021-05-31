def minAddToMakeValid(s):
    stack = []
    for ch in s:
        if ch == ')':
            if not stack or stack[-1] == ch:
                stack.append(ch)
            else:
                stack.pop()
        else:
            stack.append(ch)
#        print(ch, stack)
    return len(stack)


def main():
    print("====================================================================")
    s = input("Enter the array: ")
    y = minAddToMakeValid(s)
    print(f"Minimum number parenthesis required to make it valid:{y}")


main()
