# Day of the Year
class Solution:
    def dayOfYear(self, date: str) -> int:
        cal = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        day = 0
        y = int(date[0:4])
        m = int(date[5:7])
        d = int(date[8:])
        if y % 100 == 0:
            if y % 400 == 0:
                cal = leap
        else:
            if y % 4 == 0:
                cal = leap
        i = 0
        while i < m-1:
            day += cal[i]
            i += 1
        day += d
        return day


s = Solution()
print(s.dayOfYear(date="2019-01-09"))
print(s.dayOfYear(date="2019-02-10"))
print(s.dayOfYear(date="2003-03-01"))
print(s.dayOfYear(date="2004-03-01"))
