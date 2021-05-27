def remOutPar(s):
    stack = 0
    ret = []
    for ch in s:
        if ch == '(':
            stack += 1
            if stack != 1:
                ret.append(ch)
        else:
            stack -= 1
            if stack != 0:
                ret.append(ch)
    return ''.join(ret)


def main():
    input_str= '((()()))' #'()()' #'(()())(())'    #'(()())(())(()(()))'
    output_str = remOutPar(input_str)
    print(f"Input :",input_str)
    print(f"Output :",output_str)


main()
