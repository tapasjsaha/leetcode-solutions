#Number of 1 Bits
class Solution:
    def hammingWeight(self, n):
        # print('{:032b}'.format(n))
        cnt = 0
        while n:
            cnt += 1
            n = n & (n-1)
            # print('{:032b}'.format(n))
        return cnt

        # Good solution but not optimized as we need to repeat 32 times even if the number is zero/one
        #print('{:032b}'.format(n))
        #cnt = 0
        #musk = 1
        #for i in range(32):
        #    temp = n & musk
        #    if temp:
        #        cnt += 1
        #    n = n >> 1
        #return cnt

        # Naive solution -- Try doing it without converting it to string
        # return bin(n).count('1')   # Naive solution.


s = Solution()
print(s.hammingWeight(111))