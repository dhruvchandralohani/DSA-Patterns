"""
3Sum Closest

Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

 

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
 

Constraints:

3 <= nums.length <= 500
-1000 <= nums[i] <= 1000
-104 <= target <= 104
"""
from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()                                    # Step 1: Sort array to use two-pointer efficiently
        n = len(nums)                                  # Get array length
        result = nums[0] + nums[1] + nums[2]           # Step 2: Initialize result with sum of first 3 elements
        
        # Step 3: Fix first element (nums[i]), search for best pair in remaining
        for i in range(n - 2):                         # i goes up to n-3 (need space for j and k)
            j = i + 1                                  # Left pointer starts right after i
            k = n - 1                                  # Right pointer starts at the end
            
            # Step 4: Two-pointer search for closest sum to target
            while j < k:
                closest = nums[i] + nums[j] + nums[k]  # Current triplet sum
                
                # Step 5: Update result if current sum is closer to target
                if abs(target - closest) < abs(target - result):
                    result = closest                   # New closest sum found
                
                # Step 6: Move pointers based on comparison with target
                if closest < target:
                    j += 1                             # Sum too small → increase by moving j right
                else:
                    k -= 1                             # Sum too big (or equal) → decrease by moving k left
        
        return result                                  # Return the sum closest to target