# Given a collection of intervals, merge all overlapping intervals.

# Example 1:

# Input: [[1, 3], [2, 6], [8, 10], [15, 18]]
# Output: [[1, 6], [8, 10], [15, 18]]
# Explanation: Since intervals[1, 3] and [2, 6] overlaps, merge them into[1, 6].
# Example 2:

# Input: [[1, 4], [4, 5]]
# Output: [[1, 5]]
# Explanation: Intervals[1, 4] and [4, 5] are considered overlapping.

# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def merge(self, intervals: 'List[Interval]') -> 'List[Interval]':
        if not intervals:
            return []
        intervals.sort(key=(lambda interval: [interval.start, interval.end]))
        merged = []
        curr_interval = intervals[0]
        for idx in range(1, len(intervals)):
            if self.overlap(intervals[idx], curr_interval):
                lower = min(intervals[idx].start, curr_interval.start)
                upper = max(intervals[idx].end, curr_interval.end)
                curr_interval = Interval(lower, upper)
            else:
                merged.append(curr_interval)
                curr_interval = intervals[idx]
        merged.append(curr_interval)
        return merged

    def overlap(self, interval1, interval2):
        if interval2.start <= interval1.start <= interval2.end or interval2.start <= interval1.end <= interval2.end:
            return True
        return False

    # Alternative:
    def merge2(self, intervals):
        out = []
        for interval in sorted(intervals, key=lambda interval: interval.start):
            if out and interval.start <= out[-1].end:
                out[-1].end = max(out[-1].end, interval.end)
            else:
                out += interval,
        return out
