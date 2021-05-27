# Roman to Integer

def romanToInt(s):
    x = 0
    prev_level = 0
    dt = {'I': (1, 1), 'V': (5, 2), 'X': (10, 2), 'L': (50, 3), 'C': (100, 3), 'D': (500, 4), 'M': (1000, 4)}

    for i in range(len(s)-1, -1, -1):
        value, level = dt[s[i]]
        if level >= prev_level:
            prev_level = level
            x += value
        else:
            x -= value
    return x


def main():
    s = input("Enter Roman number: ")
    print(s)
    print(romanToInt(s))


main()