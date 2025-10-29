"""
Minimum Size Subarray Sum

Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
 

Constraints:

1 <= target <= 109
1 <= nums.length <= 105
1 <= nums[i] <= 104
 

Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).
"""
from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        Find the minimal length of a contiguous subarray with sum >= target.
        Return 0 if no such subarray exists.
        """
        # Step 1: Initialize pointers and variables
        l = 0                    # Left pointer of sliding window
        r = 0                    # Right pointer of sliding window
        n = len(nums)           # Length of input array
        s = nums[0]             # Current sum of window [l, r]
        m_sub = float("inf")    # Minimum subarray length found so far

        # Step 2: Traverse array using two pointers
        # Continue until both pointers reach the end
        while l <= n-1 and r <= n-1:
            if s < target:
                # Step 2.1: Sum is too small → expand window to the right
                r += 1
                if r <= n-1:
                    s += nums[r]  # Include new element in sum
            else:
                # Step 2.2: Sum >= target → valid window found
                # Update minimum length: current window size is (r - l + 1)
                m_sub = min(m_sub, r + 1 - l)
                
                # Shrink window from left to find smaller valid subarray
                s -= nums[l]
                l += 1
        
        # Step 3: Check if any valid subarray was found
        if m_sub == float("inf"):
            return 0  # No subarray with sum >= target
        return m_sub  # Return smallest valid length