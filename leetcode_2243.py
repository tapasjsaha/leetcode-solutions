# Calculate Digit Sum of a String
class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            res = ""
            cnt = 0
            sm = 0
            for dig in s:
                sm = sm + int(dig)
                cnt += 1
                if cnt == k:
                    res += str(sm)
                    cnt = 0
                    sm = 0
            if cnt != 0:
                res += str(sm)
            s = res
        return s


s1 = Solution()
print(s1.digitSum(s="11111222223", k=3))
print(s1.digitSum(s="00000000", k=3))
