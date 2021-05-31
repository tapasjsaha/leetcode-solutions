#Add to Array-Form of Integer

def addToArrayForm(num, k):
    n = 0
    for i in num:
        n = (n * 10) + i
    return list(str(n + k))


def main():
    num = [1, 2, 0, 0]
    k = 34
    print(addToArrayForm(num, k))


main()