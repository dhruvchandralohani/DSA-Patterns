"""
Sort Colors

Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

 

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]
 

Constraints:

n == nums.length
1 <= n <= 300
nums[i] is either 0, 1, or 2.
 

Follow up: Could you come up with a one-pass algorithm using only constant extra space?
"""
from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Sort array of 0s, 1s, and 2s in-place (Dutch National Flag Algorithm)
        Do not return anything, modify nums in-place instead.
        """
        # Step 1: Initialize three pointers
        lo = 0          # Points to the rightmost boundary of 0s (everything <= lo-1 is 0)
        mid = 0         # Current element under consideration
        hi = len(nums) - 1  # Points to the leftmost boundary of 2s (everything >= hi+1 is 2)
        
        # Step 2: Process elements until mid crosses hi
        while mid <= hi:
            if nums[mid] == 0:
                # Step 3: Found a 0 → swap with element at 'lo' pointer
                nums[lo], nums[mid] = nums[mid], nums[lo]
                # After swap: lo now points to a 1 or 2 → expand 0s region
                lo += 1
                # mid has been processed (now contains value from lo) → move forward
                mid += 1
                
            elif nums[mid] == 1:
                # Step 4: Found a 1 → already in correct region (between lo and hi)
                # Just move mid forward
                mid += 1
                
            else:  # nums[mid] == 2
                # Step 5: Found a 2 → swap with element at 'hi' pointer
                nums[hi], nums[mid] = nums[mid], nums[hi]
                # After swap: hi now contains 2 → shrink 2s region
                hi -= 1
                # DO NOT increment mid! The swapped value at mid is unknown → must recheck
                # It could be 0, 1, or 2 → let next iteration handle it
        
        # Step 6: Array is now sorted: [0s] [1s] [2s]
        # No return needed → modified in-place