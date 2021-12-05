# Binary Watch
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> [str]:
        res, vectors = [], []
        digits = [8, 4, 2, 1, 32, 16, 8, 4, 2, 1]

        def backtrack(current):
            if len(current) == 10 and current.count(1) == turnedOn:
                vectors.append(current[:])
            elif len(current) > 10 or current.count(1) > turnedOn:
                return
            else:
                candidate_list = [1, 0]
                for candidate in candidate_list:
                    backtrack(current+[candidate])

        def convert_time(vector):
            hour = sum([vector[i] * digits[i] for i in range(4)])
            mint = sum([vector[i] * digits[i] for i in range(4, 10, 1)])
            if hour > 11 or mint > 59:
                return None
            else:
                return str(hour) + ':' + str(mint).rjust(2, '0')

        backtrack([])

        for vector in vectors:
            if convert_time(vector):
                res.append(convert_time(vector))

        return res


s = Solution()
print(s.readBinaryWatch(turnedOn=1))
print(s.readBinaryWatch(turnedOn=2))
print(s.readBinaryWatch(turnedOn=9))
