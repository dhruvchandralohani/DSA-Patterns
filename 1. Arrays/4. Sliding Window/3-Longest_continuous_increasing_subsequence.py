"""
Longest Continuous Increasing Subsequence

Given an unsorted array of integers nums, return the length of the longest continuous increasing subsequence (i.e. subarray). The subsequence must be strictly increasing.

A continuous increasing subsequence is defined by two indices l and r (l < r) such that it is [nums[l], nums[l + 1], ..., nums[r - 1], nums[r]] and for each l <= i < r, nums[i] < nums[i + 1].

 

Example 1:

Input: nums = [1,3,5,4,7]
Output: 3
Explanation: The longest continuous increasing subsequence is [1,3,5] with length 3.
Even though [1,3,5,7] is an increasing subsequence, it is not continuous as elements 5 and 7 are separated by element
4.
Example 2:

Input: nums = [2,2,2,2,2]
Output: 1
Explanation: The longest continuous increasing subsequence is [2] with length 1. Note that it must be strictly
increasing.
 

Constraints:

1 <= nums.length <= 104
-109 <= nums[i] <= 109
"""
from typing import List

class Solution(object):
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        """
        Find the length of the Longest Continuously Increasing Subarray (LCIS).
        A subarray is continuous and strictly increasing: nums[i] < nums[i+1]
        """
        # Step 1: Handle edge case - empty array
        if not nums:
            return 0
        
        # Step 2: Initialize two counters
        # max_length: longest increasing subarray found so far
        # current_length: length of current increasing subarray
        max_length = 1
        current_length = 1
        
        # Step 3: Traverse array starting from index 1
        # Compare each element with its previous one
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                # Step 3.1: Current element extends the increasing sequence
                current_length += 1
                
                # Update max_length if current one is longer
                if current_length > max_length:
                    max_length = current_length
            else:
                # Step 3.2: Increasing streak is broken
                # Reset current_length to 1 (start new subarray from current element)
                current_length = 1
        
        # Step 4: Return the longest increasing subarray length
        return max_length