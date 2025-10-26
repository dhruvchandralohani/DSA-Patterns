"""
Insert Interval

You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Note that you don't need to modify intervals in-place. You can make a new array and return it.

 

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
 

Constraints:

0 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 105
intervals is sorted by starti in ascending order.
newInterval.length == 2
0 <= start <= end <= 105
"""
from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Goal: Insert newInterval into intervals and merge overlapping intervals
        
        # PHASE 1: Find the correct position to insert newInterval using Binary Search
        lo, hi = 0, len(intervals) - 1  # Step 1: Initialize binary search pointers
        
        # Step 2: Binary search to find where newInterval should be inserted
        # We want to insert at the first position where intervals[i][0] >= newInterval[0]
        while lo <= hi:
            mid = (lo + hi) // 2
            if intervals[mid][0] < newInterval[0]:
                # Current interval starts too early → search right half
                lo = mid + 1
            else:
                # Current interval starts at or after newInterval → search left half
                hi = mid - 1
        
        # Step 3: 'lo' now points to the correct insertion index
        # Insert newInterval at index 'lo'
        intervals.insert(lo, newInterval)
        
        # PHASE 2: Merge overlapping intervals (same logic as merge intervals problem)
        stack = []  # Step 4: Use stack to store merged intervals
        
        # Step 5: Iterate through all intervals (including the newly inserted one)
        for i in range(len(intervals)):
            current = intervals[i]
            
            # Step 6: Check if current overlaps with last merged interval
            if stack and current[0] <= stack[-1][1]:
                # Overlap: extend the end of last interval
                stack[-1][1] = max(stack[-1][1], current[1])
            else:
                # No overlap: add as new interval
                stack.append(current)
        
        # Step 7: Return the final merged list
        return stack