"""
Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
"""
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictn1 = {}  # Step 1: Initialize a hash map to store {number: index}
        
        # Step 2: Iterate through each element in the array with its index
        for i in range(len(nums)):
            diff = target - nums[i]  # Step 3: Compute the complement (required number to reach target)
            
            # Step 4: Check if the complement already exists in the hash map
            if diff in dictn1:
                # Step 5: Found a pair! Return indices: [index of complement, current index]
                return [dictn1[diff], i]
            
            # Step 6: If complement not found, store current number and its index
            # Key: number, Value: index (so we can retrieve it later)
            else:
                dictn1[nums[i]] = i
        
        # Note: Problem guarantees exactly one solution, so we never reach here
        return []  # (Optional: for completeness)