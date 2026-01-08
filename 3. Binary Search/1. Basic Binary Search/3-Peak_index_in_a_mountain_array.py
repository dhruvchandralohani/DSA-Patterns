"""
Peak Index in a Mountain Array

You are given an integer mountain array arr of length n where the values increase to a peak element and then decrease.

Return the index of the peak element.

Your task is to solve it in O(log(n)) time complexity.

Example 1:
Input: arr = [0,1,0]
Output: 1

Example 2:
Input: arr = [0,2,1,0]
Output: 1

Example 3:
Input: arr = [0,10,5,2]
Output: 1

Constraints:

3 <= arr.length <= 105
0 <= arr[i] <= 106
arr is guaranteed to be a mountain array.
"""
from typing import List

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        # Length of the array
        n = len(arr)

        # We start from index 1 and end at n-2 because:
        # - the peak cannot be the first element
        # - the peak cannot be the last element
        l = 1
        r = n - 2

        # Binary search to find the peak element
        while l <= r:
            # Calculate middle index
            mid = (l + r) // 2

            # Case 1: mid is greater than both neighbors
            # → this is the peak element
            if (arr[mid] > arr[mid - 1]) and (arr[mid] > arr[mid + 1]):
                return mid

            # Case 2: we are on the increasing slope
            # (mid is greater than left but smaller than right)
            # → peak lies to the right
            elif (arr[mid] > arr[mid - 1]) and (arr[mid] < arr[mid + 1]):
                l = mid + 1

            # Case 3: we are on the decreasing slope
            # → peak lies to the left
            else:
                r = mid - 1
