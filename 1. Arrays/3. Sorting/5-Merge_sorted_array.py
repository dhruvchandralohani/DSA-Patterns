"""
Merge Sorted Array

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

 

Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].
Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
 

Constraints:

nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-109 <= nums1[i], nums2[j] <= 109
 

Follow up: Can you come up with an algorithm that runs in O(m + n) time?
"""
from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        
        Merge two sorted arrays nums1 (with m valid elements) and nums2 (n elements)
        into nums1 in sorted order. nums1 has enough space (length m+n).
        """
        # Step 1: Initialize three pointers
        # i: points to the last valid element in nums1 (index m-1)
        # j: points to the last element in nums2 (index n-1)
        # k: points to the last position in nums1 where we will place the next largest value
        i = m - 1
        j = n - 1
        k = m + n - 1
        
        # Step 2: Fill nums1 from the end (largest to smallest)
        # We compare the largest remaining elements from both arrays
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                # Step 2.1: nums1 has a larger element → place it at position k
                nums1[k] = nums1[i]
                i -= 1  # Move pointer in nums1 left
            else:
                # Step 2.2: nums2 has larger (or equal) element → place it at position k
                # Also covers case when i < 0 (nums1 is exhausted)
                nums1[k] = nums2[j]
                j -= 1  # Move pointer in nums2 left
            
            # Step 2.3: Move the write pointer left after placing one element
            k -= 1
        
        # No need to handle remaining nums1 elements — they are already in place
        # If nums2 has remaining elements, they would have been copied