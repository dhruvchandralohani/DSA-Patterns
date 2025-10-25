"""
Remove Duplicates from Sorted Array

Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

Consider the number of unique elements in nums to be k. After removing duplicates, return the number of unique elements k.

The first k elements of nums should contain the unique numbers in sorted order. The remaining elements beyond index k - 1 can be ignored.

 

Example 1:

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
 

Constraints:

1 <= nums.length <= 3 * 104
-100 <= nums[i] <= 100
nums is sorted in non-decreasing order.
"""
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Edge case: If array has 0 or 1 element, no duplicates possible
        if len(nums) <= 1:
            return len(nums)
        
        # Step 1: Initialize 'i' as the position for the next unique element
        # Start from index 1 because nums[0] is always kept (first element)
        i = 1
        
        # Step 2: Traverse the array starting from index 1 using 'j'
        for j in range(1, len(nums)):
            # Step 3: Compare current element (nums[j]) with the last unique element (nums[i-1])
            if nums[j] != nums[i - 1]:
                # Step 4: Found a new unique element
                # Place it at position 'i' in the "unique" part of the array
                nums[i] = nums[j]
                # Step 5: Move the pointer 'i' forward to prepare for next unique element
                i += 1
        
        # Step 6: 'i' now represents the length of the array with unique elements
        # The first 'i' elements in nums are now unique and sorted
        return i