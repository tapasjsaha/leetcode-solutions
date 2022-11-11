# Apply Discount to Prices
class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        def discountedPrice(st):
            amt = int(st[1:])
            dp = amt - (amt * discount / 100)
            return "$" + "{:.2f}".format(dp)

        words = sentence.split(' ')
        ans = []
        for word in words:
            if word[0] == "$" and word[1:].isdigit():
                new = discountedPrice(word)
                ans.append(new)
            else:
                ans.append(word)

        return ' '.join(ans)


s = Solution()
print(s.discountPrices(sentence="there are $1 $2 and 5$ candies in the shop", discount=50))
print(s.discountPrices(sentence="1 2 $3 4 $5 $6 7 8$ $9 $10$", discount=100))
