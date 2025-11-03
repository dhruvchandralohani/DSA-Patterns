"""
Subarray Product Less Than K

Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.

 

Example 1:

Input: nums = [10,5,2,6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are:
[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
Example 2:

Input: nums = [1,2,3], k = 0
Output: 0
 

Constraints:

1 <= nums.length <= 3 * 104
1 <= nums[i] <= 1000
0 <= k <= 106
"""
from typing import List

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        """
        Count number of contiguous subarrays where product < k
        Uses Sliding Window (Two Pointers) - O(n) time
        """
        
        # Step 1: Edge case - if k <= 1, no subarray can have product < k
        # Since all nums[i] >= 1 (problem constraint), product >= 1
        if k <= 1:
            return 0
        
        # Step 2: Initialize variables
        ans = 0        # Total count of valid subarrays
        left = 0       # Left boundary of current window
        cur = 1        # Current product of window [left, right]
        
        # Step 3: Expand window with 'right' pointer
        for right in range(len(nums)):
            # Include nums[right] in current window
            cur *= nums[right]
            
            # Step 4: Shrink window from left while product >= k
            # We want product < k → if too big, remove left elements
            while cur >= k and left <= right:
                cur //= nums[left]   # Remove nums[left] from product
                left += 1            # Move left pointer right
            
            # Step 5: At this point, window [left, right] has product < k
            # All subarrays ending at 'right' and starting from 'left' to 'right' are valid
            # Number of such subarrays: (right - left + 1)
            # Example: [2,3,4], right=2, left=1 → subarrays: [3], [3,4] → 2
            ans += right - left + 1
        
        # Step 6: Return total count
        return ans