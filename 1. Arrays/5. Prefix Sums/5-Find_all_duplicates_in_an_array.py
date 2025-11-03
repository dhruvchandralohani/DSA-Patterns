"""
Find All Duplicates in an Array

Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears at most twice, return an array of all the integers that appears twice.

You must write an algorithm that runs in O(n) time and uses only constant auxiliary space, excluding the space needed to store the output

 

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [2,3]
Example 2:

Input: nums = [1,1,2]
Output: [1]
Example 3:

Input: nums = [1]
Output: []
 

Constraints:

n == nums.length
1 <= n <= 105
1 <= nums[i] <= n
Each element in nums appears once or twice.
"""
from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        """
        Find all numbers that appear TWICE in the array.
        Constraints: nums contains integers from 1 to n (n = len(nums))
        → We can use index as natural mapping!
        """
        
        # Step 1: Get length of input array
        l = len(nums)
        
        # Step 2: Create a boolean flag array of size (l+1)
        # Index 0 is unused → index i will track if number i has been seen
        # Why l+1? Because nums contains values from 1 to l
        flags = [False] * (l + 1)
        
        # Step 3: Result list to store duplicates
        ans = []
        
        # Step 4: Iterate through each number in nums
        for n in nums:
            # Step 5: Check if we've seen this number before
            if flags[n]:
                # Already seen → this is the SECOND occurrence → it's a duplicate!
                ans.append(n)
            else:
                # First time seeing this number → mark it as seen
                flags[n] = True
        
        # Step 6: Return all numbers that appeared exactly twice
        return ans