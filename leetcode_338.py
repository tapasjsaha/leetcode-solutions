# Counting Bits
class Solution:
    def countBits(self, n: int) -> [int]:
        res = [0]
        if n == 0:
            return res
        elif n == 1:
            res.append(1)
            return res
        else:
            res.append(1)
            limit = 1 << 2
            i = 0
            k = 2
            while True:
                if k < limit:
                    if k <= n:
                        res.append(1+res[i])
                        i += 1
                        k += 1
                    else:
                        break
                else:
                    limit = limit << 1
                    i = 0
            return res

s = Solution()
print(s.countBits(n=5))
