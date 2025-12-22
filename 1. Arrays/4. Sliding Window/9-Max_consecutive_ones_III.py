"""
Max Consecutive Ones III

Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
 
Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
0 <= k <= nums.length
"""
from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        """
        Find the length of the longest subarray containing at most k zeros
        after flipping any number (up to k) of zeros to ones.
        
        Sliding window technique: maintain a window [l, r] where the number of zeros <= k.
        """
        l = 0                    # Left pointer of the sliding window
        maxLength = 0            # Maximum length of valid subarray found
        zeroCount = 0            # Count of zeros in the current window [l, r]
        n = len(nums)            # Length of the input array
        
        # Step 1: Expand the window using right pointer
        for r in range(n):
            # If current element is 0, increment zero count
            if nums[r] == 0:
                zeroCount += 1
            
            # Step 2: Shrink window from left if number of zeros exceeds k
            # This means we would need more than k flips to make the window all ones
            while zeroCount > k:
                # Remove the leftmost element
                if nums[l] == 0:
                    zeroCount -= 1   # Only decrement if it was a zero
                l += 1               # Move left pointer right
            
            # Step 3: Current window [l, r] has at most k zeros → valid
            # Update maximum length
            maxLength = max(maxLength, r - l + 1)
        
        # Step 4: Return the longest valid subarray length
        return maxLength