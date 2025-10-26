"""
Interval List Intersections

You are given two lists of closed intervals, firstList and secondList, where firstList[i] = [starti, endi] and secondList[j] = [startj, endj]. Each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

A closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.

The intersection of two closed intervals is a set of real numbers that are either empty or represented as a closed interval. For example, the intersection of [1, 3] and [2, 4] is [2, 3].

 

Example 1:


Input: firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
Example 2:

Input: firstList = [[1,3],[5,9]], secondList = []
Output: []
 

Constraints:

0 <= firstList.length, secondList.length <= 1000
firstList.length + secondList.length >= 1
0 <= starti < endi <= 109
endi < starti+1
0 <= startj < endj <= 109 
endj < startj+1
"""
from typing import List

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        # Goal: Find all overlapping intervals between two lists of intervals
        
        # Step 1: Initialize two pointers for both lists
        i = 0  # Pointer for firstList
        j = 0  # Pointer for secondList
        
        # Step 2: Result list to store all intersection intervals
        result = []
        
        # Step 3: Traverse both lists while there are intervals to compare
        while i < len(firstList) and j < len(secondList):
            # Step 4: Extract current intervals from both lists
            first_start, first_end = firstList[i]
            second_start, second_end = secondList[j]
            
            # Step 5: Compute potential intersection
            # Intersection exists between [max(start1, start2), min(end1, end2)]
            start = max(first_start, second_start)
            end = min(first_end, second_end)
            
            # Step 6: If start <= end → valid intersection → add to result
            if start <= end:
                result.append([start, end])
            
            # Step 7: Move the pointer of the interval that ENDS EARLIER
            # This is key: we can discard the interval that finishes first
            # because any future overlap must involve the other one
            if first_end < second_end:
                i += 1  # firstList interval ends earlier → move i
            else:
                j += 1  # secondList interval ends earlier (or equal) → move j
        
        # Step 8: Return all found intersection intervals
        return result