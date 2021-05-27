dict = {
    1: 'I',
    4: 'IV',
    5: 'V',
    9: 'IX',
    10: 'X',
    40: 'XL',
    50: 'L',
    90: 'XC',
    100: 'C',
    400: 'CD',
    500: 'D',
    900: 'CM',
    1000: 'M'
}

min_list = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]


def convertRoman(num):
    y = ''
    while num != 0:
        for i in range(len(min_list)):
            if num - min_list[i] >= 0:
                y = y + dict[min_list[i]]
                num -= min_list[i]
                break
            else:
                continue
    return y


def main():
    print("====================================================================")
    while True:
        inp = input("Enter Number: ")
        if inp.isdigit():
            x = int(inp)
            y = convertRoman(x)
            print(f"Corresponding Roman number is :{y}")
        else:
            break


main()
