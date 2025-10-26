"""
Non-overlapping Intervals

Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Note that intervals which only touch at a point are non-overlapping. For example, [1, 2] and [2, 3] are non-overlapping.

 

Example 1:

Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
Example 2:

Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.
Example 3:

Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
 

Constraints:

1 <= intervals.length <= 105
intervals[i].length == 2
-5 * 104 <= starti < endi <= 5 * 104
"""
from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Goal: Return the MINIMUM number of intervals to REMOVE to make the rest non-overlapping
        
        # Step 1: Handle edge case - if 0 or 1 interval, no overlaps possible
        if len(intervals) <= 1:
            return 0
        
        # Step 2: Sort intervals by START time (default sort on first element)
        # This allows us to process intervals in chronological order
        intervals.sort(key=lambda x: x[0])
        
        # Step 3: Initialize counter for intervals that must be removed
        notNeeded = 0
        
        # Step 4: Track the end time of the last non-removed interval
        # Start with the end of the first interval
        prev_end = intervals[0][1]
        
        # Step 5: Iterate through all intervals starting from index 1
        for i in range(1, len(intervals)):
            current_start = intervals[i][0]
            current_end   = intervals[i][1]
            
            # Step 6: Check for overlap with previous kept interval
            if prev_end > current_start:
                # Overlap detected: we must remove one interval
                notNeeded += 1
                
                # Greedy choice: Keep the interval that ENDS EARLIER
                # This maximizes space for future intervals
                prev_end = min(prev_end, current_end)
            else:
                # No overlap: we can keep current interval
                # Update prev_end to current interval's end
                prev_end = current_end
        
        # Step 7: Return total number of intervals removed
        return notNeeded