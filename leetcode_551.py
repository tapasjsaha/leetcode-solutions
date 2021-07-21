#Student Attendance Record I
class Solution:
    def checkRecord(self, s):
        if s.count('A') < 2 and 'LLL' not in s:
            return True
        else:
            return False


s = Solution()
print(s.checkRecord(s = "PPALLP"))
print(s.checkRecord(s = "PPALLL"))
print(s.checkRecord(s = "PAPALLP"))
print(s.checkRecord(s = "PPLALLP")) #check this test case in leetcode