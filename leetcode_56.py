# Merge Intervals
class Solution:
    def merge(self, intervals: [[int]]) -> [[int]]:
        res = []
        sorted_intervals = sorted(intervals, key=lambda x: x[0], reverse=False)
        current_interval = sorted_intervals[0]
        for next_interval in sorted_intervals[1:]:
            if current_interval[1] >= next_interval[0]:
                current_interval[1] = max(current_interval[1], next_interval[1])
            else:
                res.append(current_interval)
                current_interval = next_interval
        res.append(current_interval)

        return res


s = Solution()
print(s.merge(intervals=[[1, 3], [2, 6], [15, 18], [8, 10], [10, 12]]))
print(s.merge(intervals=[[1, 3]]))
print(s.merge(intervals=[[1, 4], [2, 3]]))
