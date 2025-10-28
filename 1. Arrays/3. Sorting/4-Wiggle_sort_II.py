"""
Wiggle Sort II

Given an integer array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....

You may assume the input array always has a valid answer.

 

Example 1:

Input: nums = [1,5,1,1,6,4]
Output: [1,6,1,5,1,4]
Explanation: [1,4,1,5,1,6] is also accepted.
Example 2:

Input: nums = [1,3,2,2,3,1]
Output: [2,3,1,3,1,2]
 

Constraints:

1 <= nums.length <= 5 * 104
0 <= nums[i] <= 5000
It is guaranteed that there will be an answer for the given input nums.
 

Follow Up: Can you do it in O(n) time and/or in-place with O(1) extra space?
"""
from typing import List

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        Rearrange array such that: nums[0] < nums[1] > nums[2] < nums[3] > ...
        """
        # Step 1: Get length of array
        n = len(nums)
        
        # Step 2: Sort the array in ascending order
        # This groups smaller and larger numbers together for alternating placement
        nums.sort()
        
        # Step 3: Find the median index (largest index in the smaller half)
        # For n = 5: indices [0,1,2,3,4] → mid = (5-1)//2 = 2 → nums[2] is median
        # Smaller half: [0,1,2], Larger half: [3,4]
        mid = (n - 1) // 2
        
        # Step 4: Reconstruct array using clever slicing and reversal
        # nums[::2]  → even indices: 0,2,4,... → place smaller numbers (in reverse)
        # nums[1::2] → odd indices:  1,3,5,... → place larger numbers (in reverse)
        #
        # nums[mid::-1] → from mid down to 0 → reversed smaller half
        # nums[:mid:-1] → from end down to mid+1 → reversed larger half
        #
        # Reversing both halves prevents equal adjacent elements from violating wiggle
        nums[::2], nums[1::2] = nums[mid::-1], nums[:mid:-1]
        
        # Final array satisfies: nums[0] < nums[1] > nums[2] < nums[3] > ...