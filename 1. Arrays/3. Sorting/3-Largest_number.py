"""
Largest Number

Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

Since the result may be very large, so you need to return a string instead of an integer.

 

Example 1:

Input: nums = [10,2]
Output: "210"
Example 2:

Input: nums = [3,30,34,5,9]
Output: "9534330"
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 109
"""
from typing import List

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Step 1: Convert all integers to strings
        # We need strings to compare digits when concatenating
        array = list(map(str, nums))
        
        # Step 2: Custom sort using a special comparison rule
        # Key idea: for two numbers a and b, compare (a+b) vs (b+a)
        # But to avoid string concatenation in every comparison, use x*10
        # Example: "3" and "30" → "3"*10 = "3333333333" > "30"*10 = "3030303030" → 3 comes first
        array.sort(key=lambda x: x*10, reverse=True)
        
        # Step 3: Handle edge case where result should be "0"
        # If the largest element is "0", all numbers are 0 → return "0"
        if array[0] == "0":
            return "0"
        
        # Step 4: Join all sorted strings to form the largest number
        largest = ''.join(array)
        
        # Step 5: Return the result as a string
        return largest