"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = [interval.start for interval in intervals]
        ends = [interval.end for interval in intervals]
        starts.sort()
        ends.sort()
        i, j, n = 0, 0, len(starts)
        ans, cur = 0, 0
        while i < n and j < n:
            if starts[i] < ends[j]:
                cur += 1
                i += 1
                ans = max(ans, cur)
            else:
                j += 1
                cur -= 1
        return ans