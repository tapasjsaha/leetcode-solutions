#Self Dividing Numbers
import time


def is_self_dividing(num):
    if '0' in str(num):
        return False
    else:
        for ch in str(num):
            if num % int(ch) != 0:
                return False
        return True


def selfDividingNumbers(left, right):
    return [num for num in range(left, right+1, 1) if is_self_dividing(num)]


def main():
    st = time.time()
    left = 1
    right = 1000
    #print(is_self_dividing(14))
    print(selfDividingNumbers(left, right))
    en = time.time()
    print(en -st)


main()