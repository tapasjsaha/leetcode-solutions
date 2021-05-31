def bitwiseComplement(n):
    a_bin = bin(n)[2:]
    l = len(a_bin)
    b_bin = '1' * l
    c_lst = []
    for i in range(l):
        c_lst.append(str(int(a_bin[i]) ^ int(b_bin[i])))
    c_bin = ''.join(c_lst)
    return int(c_bin, 2)


def main():
    print("====================================================================")
    x = int(input("Enter Number: "))
    y = bitwiseComplement(x)
    print(f"Complement number is :{y}")


main()
