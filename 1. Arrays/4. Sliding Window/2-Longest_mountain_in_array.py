"""
Longest Mountain in Array

You may recall that an array arr is a mountain array if and only if:

arr.length >= 3
There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
Given an integer array arr, return the length of the longest subarray, which is a mountain. Return 0 if there is no mountain subarray.

 

Example 1:

Input: arr = [2,1,4,7,3,2,5]
Output: 5
Explanation: The largest mountain is [1,4,7,3,2] which has length 5.
Example 2:

Input: arr = [2,2,2]
Output: 0
Explanation: There is no mountain.
 

Constraints:

1 <= arr.length <= 104
0 <= arr[i] <= 104
 

Follow up:

Can you solve it using only one pass?
Can you solve it in O(1) space?
"""
from typing import List

class Solution:
    def longestMountain(self, A: List[int]) -> int:
        """
        Find the length of the longest mountain subarray.
        A mountain has: strictly increasing -> peak -> strictly decreasing
        Minimum length: 3 (e.g., [1,2,1])
        """
        # Step 1: Initialize tracking variables
        # ans: longest mountain length found so far
        # start: index where current mountain candidate begins (base of uphill)
        ans, start = 0, None
        
        # Step 2: Iterate through array starting from index 1
        # We compare A[i] with A[i-1] to detect slope changes
        for i in range(1, len(A)):
            # Step 3: Detect the start of an uphill (increasing slope)
            # Conditions:
            # - A[i] > A[i-1]: current element is greater → going up
            # - (i == 1 or A[i-1] <= A[i-2]): either first pair, or previous was not increasing
            #   → ensures we start a new mountain after a flat or downhill
            if A[i] > A[i-1] and (i == 1 or A[i-1] <= A[i-2]):
                start = i - 1  # Mark mountain base at i-1
            
            # Step 4: Handle flat terrain (equal elements)
            # A mountain cannot have equal adjacent elements
            # Reset start → break any ongoing mountain
            elif A[i] == A[i-1]:
                start = None 
            
            # Step 5: Detect downhill after a valid uphill
            # Conditions:
            # - A[i] < A[i-1]: current element is smaller → going down
            # - start is not None: we have a valid uphill started
            # → Then we have a full mountain from start to i
            elif A[i] < A[i-1] and start is not None:
                # Calculate mountain length: from base (start) to current (i)
                current_length = i - start + 1
                ans = max(ans, current_length)
                # Note: start remains valid — downhill can continue
                # But we don't reset start here — allows extending the same mountain
        
        # Step 6: Return the longest mountain found
        return ans