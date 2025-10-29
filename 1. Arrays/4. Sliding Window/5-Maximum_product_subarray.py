"""
Maximum Product Subarray

Given an integer array nums, find a subarray that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

Note that the product of an array with a single element is the value of that element.

 

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
 

Constraints:

1 <= nums.length <= 2 * 104
-10 <= nums[i] <= 10
The product of any subarray of nums is guaranteed to fit in a 32-bit integer.
"""
from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        Find the maximum product of a contiguous subarray (including negative numbers and zeros).
        """
        n = len(nums)
        best = float("-inf")        # Step 1: Track the global maximum product
        product = 1                 # Step 2: Current product of the window [l, r]
        l = 0                       # Step 3: Left pointer of the sliding window
        
        # Step 4: Main loop — expand right pointer
        for r in range(n):
            # Step 4.1: If multiplying by nums[r] gives 0, we hit a zero
            # This breaks the current subarray
            if product * nums[r] != 0:
                product *= nums[r]  # Continue extending current product
            else:
                # Step 4.2: Zero encountered — current subarray ends
                # Shrink from left to remove elements before the zero
                while l < r - 1:
                    if nums[l] == 0:
                        # Skip zeros on the left — they reset product anyway
                        l += 1
                    else:
                        # Remove nums[l] from product by dividing
                        product /= nums[l]
                        l += 1
                        # Update best if current subarray (after removal) is better
                        if product > best:
                            best = product
                # Reset product to start fresh from current element (nums[r])
                product = nums[r]
                l = r  # New window starts at r
        
            # Step 4.3: Update global best with current product
            if product > best:
                best = product

        # Step 5: After loop, shrink remaining window from left
        # This handles the last subarray ending at nums[n-1]
        while l < r:
            if nums[l] == 0:
                l += 1  # Skip zero
            else:
                product /= nums[l]
                l += 1
                if product > best:
                    best = product

        # Step 6: Return result as integer
        return int(best)