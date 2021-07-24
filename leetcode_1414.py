#Find the Minimum Number of Fibonacci Numbers Whose Sum Is K
class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        f1, f2, nxt = 0, 1, 0
        f_lst = []
        while nxt <= k:
            f_lst.append(f2)
            nxt = f1 + f2
            f1 = f2
            f2 = nxt

        f_lst.sort(reverse=True)
        #print(f_lst)
        i, count = 0, 0
        #l = [] #Just for debug purpose
        while k > 0:
            if k >= f_lst[i]:
                count += 1
                k = k - f_lst[i]
                #l.append(f_lst[i]) #Just for debug purpose
            else:
                i += 1

        #print(l) #Just for debug purpose
        return count


s = Solution()
print(s.findMinFibonacciNumbers(7))
print(s.findMinFibonacciNumbers(10))
print(s.findMinFibonacciNumbers(19))
print(s.findMinFibonacciNumbers(1000))
