"""
Squares of a Sorted Array

Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

 

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.
 

Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?
"""
from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)                              # Step 1: Get length of input array
        
        # Step 2: Initialize two pointers
        left = 0                                   # Points to start (smallest index)
        right = n - 1                              # Points to end (largest index)
        
        # Step 3: Pre-allocate result array of size n, filled with zeros
        res = [0] * n
        
        # Step 4: Fill result from RIGHT to LEFT (largest to smallest squares)
        # i goes from n-1 down to 0
        for i in range(n - 1, -1, -1):
            # Step 5: Compare absolute values at left and right
            if abs(nums[left]) < abs(nums[right]):
                # Right element has larger magnitude → its square is larger
                res[i] = nums[right] ** 2
                right -= 1                     # Move right pointer left
            else:
                # Left element has larger or equal magnitude
                res[i] = nums[left] ** 2
                left += 1                      # Move left pointer right
        
        # Step 6: Result array now contains squares in sorted order
        return res