"""
Count of Range Sum

Given an integer array nums and two integers lower and upper, return the number of range sums that lie in [lower, upper] inclusive.

Range sum S(i, j) is defined as the sum of the elements in nums between indices i and j inclusive, where i <= j.

 

Example 1:

Input: nums = [-2,5,-1], lower = -2, upper = 2
Output: 3
Explanation: The three ranges are: [0,0], [2,2], and [0,2] and their respective sums are: -2, -1, 2.
Example 2:

Input: nums = [0], lower = 0, upper = 0
Output: 1
 

Constraints:

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
-105 <= lower <= upper <= 105
The answer is guaranteed to fit in a 32-bit integer.
"""
from typing import List

class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        """
        Count subarrays whose sum is in [lower, upper] using Merge Sort.
        Key Idea: Use prefix sums + count valid pairs during merge.
        """
        
        # PHASE 1: Build prefix sum array (cumsum)
        # cumsum[i] = sum of nums[0..i-1]
        # So, sum of subarray nums[i..j] = cumsum[j+1] - cumsum[i]
        cumsum = [0]  # Start with 0 for empty subarray
        for n in nums:
            cumsum.append(cumsum[-1] + n)
        # Example: nums = [1,2,3] → cumsum = [0,1,3,6]
        
        # PHASE 2: Modified Merge Sort with counting
        # We sort cumsum and count valid (left, right) pairs where:
        # lower <= cumsum[right] - cumsum[left] <= upper
        # → lower + cumsum[left] <= cumsum[right] <= upper + cumsum[left]
        def mergesort(l, r):
            # Base case: single element → no subarray
            if l == r:
                return 0
            
            # Step 1: Divide
            mid = (l + r) // 2
            # Recursively count in left and right halves
            cnt = mergesort(l, mid) + mergesort(mid + 1, r)
            
            # Step 2: Count valid pairs across halves using two pointers
            i = j = mid + 1  # Start from right half
            
            # For each left value in [l, mid], find range [i, j) in right half
            for left in cumsum[l:mid + 1]:
                # Find first i where cumsum[i] >= lower + left
                while i <= r and cumsum[i] - left < lower:
                    i += 1
                # Find first j where cumsum[j] > upper + left
                while j <= r and cumsum[j] - left <= upper:
                    j += 1
                # All indices from i to j-1 satisfy: lower <= sum <= upper
                cnt += j - i
            
            # Step 3: Merge and sort the current range [l, r]
            # This ensures subarrays are processed in sorted order
            cumsum[l:r + 1] = sorted(cumsum[l:r + 1])
            
            return cnt
        
        # Start merge sort on entire cumsum array (0 to len-1)
        return mergesort(0, len(cumsum) - 1)