# Integer to English Words
class Solution:
    def numToWordsHundred(self, num: int) -> str:
        ones = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight",
                9: "Nine"}
        tens = {10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", 15: "Fifteen", 16: "Sixteen",
                17: "Seventeen", 18: "Eighteen", 19: "Nineteen"}
        tys = {2: "Twenty", 3: "Thirty", 4: "Forty", 5: "Fifty", 6: "Sixty", 7: "Seventy", 8: "Eighty", 9: "Ninety"}
        res = ""
        if num//100 > 0:
            res += "" if res == "" else " "
            res += ones[num//100] + " Hundred"
            num = num % 100
        if num//10 == 1:
            res += "" if res == "" else " "
            res += tens[num]
        else:
            if num//10 > 1:
                res += "" if res == "" else " "
                res += tys[num // 10]
                num = num % 10
            if num > 0:
                res += "" if res == "" else " "
                res += ones[num]
        return res


    def numberToWords(self, num: int) -> str:
        res = ""
        if num == 0:
            return "Zero"
        if num//1000000000 > 0:
            res += "" if res == "" else " "
            res += self.numToWordsHundred(num//1000000000) + " Billion"
            num = num % 1000000000
        if num//1000000 > 0:
            res += "" if res == "" else " "
            res += self.numToWordsHundred(num//1000000) + " Million"
            num = num % 1000000
        if num//1000 > 0:
            res += "" if res == "" else " "
            res += self.numToWordsHundred(num//1000) + " Thousand"
            num = num % 1000
        res += "" if res == "" else " "
        res += self.numToWordsHundred(num)
        return res.strip()


s = Solution()
x = int(input("Enter Number:"))
print(s.numberToWords(x))
#print(s.numberToWords(num=0))
#print(s.numberToWords(num=5))
#print(s.numberToWords(num=10))
#print(s.numberToWords(num=15))
#print(s.numberToWords(num=35))
#print(s.numberToWords(num=100))
#print(s.numberToWords(num=515))
#print(s.numberToWords(num=525))
#print(s.numberToWords(num=1000))
#print(s.numberToWords(num=1515))
#print(s.numberToWords(num=1525))
#print(s.numberToWords(num=10515))
#print(s.numberToWords(num=21525))
#print(s.numberToWords(num=100000))
#print(s.numberToWords(num=100515))
#print(s.numberToWords(num=215525))
#print(s.numberToWords(num=1010515))
#print(s.numberToWords(num=2125525))
#print(s.numberToWords(num=1000000))
#print(s.numberToWords(num=1234567))
#print(s.numberToWords(num=1234567891))
#print(s.numberToWords(num=1000000000))

