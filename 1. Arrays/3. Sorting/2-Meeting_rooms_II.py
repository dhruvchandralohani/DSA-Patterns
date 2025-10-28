"""
Meeting Rooms II

Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (s < e), find the minimum number of conference rooms required.

Examples:
Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Explanation: A room is needed for [0, 30] and another room for [5, 10], [15, 20].
Example 2:

Input: [[7,10],[2,4]]
Output: 1
Explanation: Only one room is needed as [7,10] overlaps with [2,4].
Example 3:

Input: [[0, 5],[2, 6],[3, 7],[4, 8]]
Output: 4
Explanation: At one point, all four meetings overlap (between time 4 and 5). Therefore, four rooms are required to accommodate them.


Constraints:

1 <= intervals.length <= 10^4
0 <= s < e <= 10^9
"""
from typing import List

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # Step 1: Handle edge case
        # If no meetings, no rooms needed
        if not intervals:
            return 0
        
        # Step 2: Extract start and end times into separate arrays
        # This allows us to process them independently using two pointers
        n = len(intervals)
        starts = [interval[0] for interval in intervals]  # All start times
        ends = [interval[1] for interval in intervals]    # All end times
        
        # Step 3: Sort both arrays
        # Sorting helps us process events in chronological order
        starts.sort()
        ends.sort()
        
        # Step 4: Initialize variables
        # - rooms: current number of active meetings (rooms in use)
        # - max_rooms: maximum rooms needed at any time
        # - i: pointer for start times
        # - j: pointer for end times
        rooms = 0
        max_rooms = 0
        i, j = 0, 0
        
        # Step 5: Traverse using two pointers
        # Compare next start time with next end time
        while i < n:
            if starts[i] < ends[j]:
                # Step 5.1: A meeting starts before the next one ends
                # Need a new room
                rooms += 1
                max_rooms = max(max_rooms, rooms)  # Update peak usage
                i += 1  # Move to next start
            else:
                # Step 5.2: A meeting ends before or when the next starts
                # A room becomes available
                rooms -= 1
                j += 1  # Move to next end
        
        # Step 6: Return the maximum number of rooms used at any point
        return max_rooms