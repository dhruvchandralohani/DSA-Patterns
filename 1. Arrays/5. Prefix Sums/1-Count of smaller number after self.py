"""
Count of Smaller Numbers After Self

Given an integer array nums, return an integer array counts where counts[i] is the number of smaller elements to the right of nums[i].

 

Example 1:

Input: nums = [5,2,6,1]
Output: [2,1,1,0]
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
Example 2:

Input: nums = [-1]
Output: [0]
Example 3:

Input: nums = [-1,-1]
Output: [0,0]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
"""
from typing import List

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        """
        For each nums[i], count how many elements to its RIGHT are strictly SMALLER.
        Uses: Coordinate Compression + Fenwick Tree (BIT)
        """
        
        # PHASE 1: Coordinate Compression (Rank Mapping)
        # Step 1: Get unique values and sort them
        unique_vals = sorted(set(nums))  # Remove duplicates and sort → [1, 2, 3, 5]
        
        # Step 2: Map each value to its rank (1-based index for BIT)
        # Why 1-based? BIT uses 1-based indexing
        mapping = {v: i + 1 for i, v in enumerate(unique_vals)}
        # Example: {1:1, 2:2, 3:3, 5:4}
        
        size_vals = len(unique_vals) + 1  # BIT size (1 extra for 1-based indexing)
        size_nums = len(nums)
        
        # Step 3: Initialize Binary Indexed Tree (Fenwick Tree)
        # Stores frequency of ranks seen so far
        bit = [0] * size_vals
        
        # Step 4: Result array to store count of smaller elements to the right
        result = [0] * size_nums
        
        # PHASE 2: Process elements from RIGHT to LEFT
        # Why right to left? Because we count elements to the right
        for idx in range(size_nums - 1, -1, -1):
            n = mapping[nums[idx]]  # Get rank of current number (1-based)
            
            # Step 5: QUERY - Count how many numbers SMALLER than current have been seen
            # We query sum of frequencies from rank 1 to (n-1)
            temp = 0
            i = n - 1  # We want sum up to rank (n-1)
            while i > 0:
                temp += bit[i]           # Add frequency at index i
                i = i - (i & -i)         # Move to parent in BIT tree
            result[idx] = temp           # Store count of smaller elements to the right
            
            # Step 6: UPDATE - Add current number's rank to BIT
            # Mark that we've seen one occurrence of this rank
            i = n
            while i < size_vals:
                bit[i] += 1              # Increment frequency
                i = i + (i & -i)         # Move to next node that covers this index
        
        # Step 7: Return result
        return result