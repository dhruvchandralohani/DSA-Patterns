"""
Search Insert Position

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104
"""
from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Length of the input array
        n = len(nums)

        # Initialize left and right pointers for binary search
        l = 0
        r = n - 1

        # Perform binary search while the search space is valid
        while l <= r:
            # Calculate the middle index
            mid = (l + r) // 2

            # If the middle element is the target, return its index
            if nums[mid] == target:
                return mid

            # If the middle element is greater than target,
            # discard the right half (including mid)
            elif nums[mid] > target:
                r = mid - 1

            # If the middle element is smaller than target,
            # discard the left half (including mid)
            else:
                l = mid + 1

        # If target is not found, `l` will be the correct insertion position
        # because:
        # - all elements before index `l` are smaller than target
        # - all elements from index `l` onwards are greater than target
        return l
