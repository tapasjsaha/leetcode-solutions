# Non-overlapping Intervals
class Solution:
    def eraseOverlapIntervals(self, intervals: [[int]]) -> int:
        intervals.sort(key=lambda x:x[0], reverse=False)
        overlap = 0
        end = intervals[0][1]
        for interval in intervals[1:]:
            if interval[0] < end:
                overlap += 1
                end = min(end, interval[1])  # Greedy: take whichever interval end early to avoid future overlap
            else:
                end = interval[1]  # No overlap, so modify end to end of next interval

        return overlap


s = Solution()
print(s.eraseOverlapIntervals(intervals=[[1, 2]]))
print(s.eraseOverlapIntervals(intervals=[[1, 2], [2, 3]]))
print(s.eraseOverlapIntervals(intervals=[[1, 2], [2, 3], [3, 4], [1, 3]]))
print(s.eraseOverlapIntervals(intervals=[[1, 2], [1, 2], [1, 2]]))
