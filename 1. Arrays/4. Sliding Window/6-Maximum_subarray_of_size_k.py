"""
Max Sum Subarray of size K

Given an array of integers arr[]  and a number k. Return the maximum sum of a subarray of size k.

Note: A subarray is a contiguous part of any given array.

Examples:

Input: arr[] = [100, 200, 300, 400], k = 2
Output: 700
Explanation: arr2 + arr3 = 700, which is maximum.

Input: arr[] = [1, 4, 2, 10, 23, 3, 1, 0, 20], k = 4
Output: 39
Explanation: arr1 + arr2 + arr3 + arr4 = 39, which is maximum.

Input: arr[] = [100, 200, 300, 400], k = 1
Output: 400
Explanation: arr3 = 400, which is maximum.

Constraints:
1 ≤ arr.size() ≤ 106
1 ≤ arr[i] ≤ 106
1 ≤ k ≤ arr.size()
"""
class Solution:
    def maxSubarraySum(self, arr, k):
        """
        Find the maximum sum of any contiguous subarray of size exactly k.
        Uses sliding window technique for O(n) time.
        """
        n = len(arr)
        
        # Step 1: Handle edge case - if array is smaller than k, no valid window
        if n < k:
            return 0
        
        # Step 2: Calculate sum of the first window of size k
        res = sum(arr[:k])      # Initial window sum: arr[0] to arr[k-1]
        low = 0                 # Left boundary of current window
        high = k                # Right boundary (exclusive) of current window
        
        # Step 3: Initialize answer with the first window sum
        ans = res
        
        # Step 4: Slide the window across the array
        # Move from window [0:k] to [1:k+1], ..., up to [n-k:n]
        while high < n:
            # Update current window sum:
            # Add new element on the right, remove element going out on the left
            ans = ans + arr[high] - arr[low]
            
            # Update maximum sum found so far
            if ans > res:
                res = ans
            
            # Move the window one step to the right
            low += 1
            high += 1
        
        # Step 5: Return the maximum sum of any subarray of size k
        return res