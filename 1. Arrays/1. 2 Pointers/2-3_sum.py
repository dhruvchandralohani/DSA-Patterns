"""
3Sum

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 

Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105
"""
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)           # Get the length of the input array
        res = []                # Initialize result list to store valid triplets
        nums.sort()             # Sort the array: enables two-pointer and duplicate skipping
        
        # Outer loop: Fix the first element (nums[i])
        for i in range(n):
            # Skip duplicate values for nums[i] to avoid duplicate triplets
            # Only check if i > 0 to allow the first occurrence
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Two pointers: left starts right after i, right at the end
            j = i + 1
            k = n - 1
            
            # Inner loop: Find two numbers in [i+1, n-1] that sum to -nums[i]
            while j < k:
                total = nums[i] + nums[j] + nums[k]  # Current sum of triplet
                
                # If sum is too large, decrease the largest number
                if total > 0:
                    k -= 1
                # If sum is too small, increase the smallest number
                elif total < 0:
                    j += 1
                # Found a valid triplet: [nums[i], nums[j], nums[k]]
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    
                    # Move left pointer forward
                    j += 1
                    # Skip duplicates for nums[j] to avoid repeated triplets
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    # Note: We don't need to skip k duplicates here because
                    # we're moving j forward and k will be adjusted naturally
        
        return res  # Return all unique triplets that sum to zero