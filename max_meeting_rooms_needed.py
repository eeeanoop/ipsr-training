"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start_timings = sorted([ i.start for i in intervals ])
        end_timings = sorted([ i.end for i in intervals ])

        current_room_count = 0
        max_rooms = 0

        # Two pointers
        start_ptr = 0
        end_ptr = 0

        while start_ptr < len(intervals):

            if start_timings[start_ptr] < end_timings[end_ptr]:
                # Meeting are overlapping, need extra room
                current_room_count += 1
                start_ptr += 1
            else:
                # One meeting ended, we can reuse the room
                current_room_count -= 1
                end_ptr += 1
            max_rooms = max(current_room_count, max_rooms)

        return max_rooms


        