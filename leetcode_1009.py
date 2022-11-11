# Complement of Base 10 Integer
class Solution:
    def bitwiseComplement(self, n: int) -> int:
        x, y = 0, n
        while y != 0:
            x += 1
            y = y >> 1
        return ((1 << x) - 1) ^ n if x != 0 else 1


s = Solution()
print(s.bitwiseComplement(n=5))
print(s.bitwiseComplement(n=7))
print(s.bitwiseComplement(n=10))
print(s.bitwiseComplement(n=0))


# def bitwiseComplement(n):
#     a_bin = bin(n)[2:]
#     l = len(a_bin)
#     b_bin = '1' * l
#     c_lst = []
#     for i in range(l):
#         c_lst.append(str(int(a_bin[i]) ^ int(b_bin[i])))
#     c_bin = ''.join(c_lst)
#     return int(c_bin, 2)
#
#
# def main():
#     print("====================================================================")
#     x = int(input("Enter Number: "))
#     y = bitwiseComplement(x)
#     print(f"Complement number is :{y}")
#
#
# main()
