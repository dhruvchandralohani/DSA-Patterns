"""
Merge Intervals

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
Example 3:

Input: intervals = [[4,7],[1,4]]
Output: [[1,7]]
Explanation: Intervals [1,4] and [4,7] are considered overlapping.
 

Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
"""
from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Step 1: Handle edge case - if input is empty, return empty list
        if not intervals:
            return []
        
        # Step 2: Sort intervals by start time (first element of each interval)
        # This ensures we process intervals in order of increasing start points
        intervals.sort(key=lambda x: x[0])
        
        # Step 3: Initialize stack to store merged intervals
        # We'll use a list as a stack (append/pop from end)
        stack = []
        
        # Step 4: Iterate through each interval in sorted order
        for i in range(len(intervals)):
            current = intervals[i]  # Current interval being processed
            
            # Step 5: Check if stack is not empty AND last merged interval overlaps with current
            # Overlap condition: end of last interval >= start of current interval
            if stack and stack[-1][1] >= current[0]:
                # Step 6: Merge overlapping intervals
                # Update end of last interval to be the max of its end and current's end
                stack[-1][1] = max(stack[-1][1], current[1])
            else:
                # Step 7: No overlap → add current interval to stack as a new merged interval
                stack.append(current)
        
        # Step 8: Stack now contains all merged non-overlapping intervals
        return stack