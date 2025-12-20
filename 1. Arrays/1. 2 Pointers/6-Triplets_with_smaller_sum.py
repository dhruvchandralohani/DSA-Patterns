"""
Given an array arr[] of distinct integers of size n and a value sum, the task is to find the count of triplets (i, j, k), having (i<j<k) with the sum of (arr[i] + arr[j] + arr[k]) smaller than the given value sum.


Examples :


Input: n = 4, sum = 2, arr[] = {-2, 0, 1, 3}
Output:  2
Explanation: Below are triplets with sum less than 2 (-2, 0, 1) and (-2, 0, 3). 

Input: n = 5, sum = 12, arr[] = {5, 1, 3, 4, 7}
Output: 4
Explanation: Below are triplets with sum less than 12 (1, 3, 4), (1, 3, 5), (1, 3, 7) and (1, 4, 5).

Expected Time Complexity: O(N2).
Expected Auxiliary Space: O(1).


Constraints:
3 ≤ N ≤ 103
-103 ≤ arr[i] ≤ 103
"""
from typing import List

class Solution:
    def countTriplets(self, n: int, sum: int, arr: List[int]) -> int:
        """
        Count the number of triplets (i, j, k) such that:
        i < j < k and arr[i] + arr[j] + arr[k] < sum
        """
        # Step 1: Sort the array
        # This allows us to use two-pointer technique efficiently
        arr.sort()
        count = 0     # Total number of valid triplets
        
        # Step 2: Fix the largest element of the triplet (arr[i])
        # We iterate i from 0 to n-3 (since we need at least two elements after i)
        for i in range(n - 2):
            # Step 3: Set two pointers for the remaining range [i+1, n-1]
            j = i + 1      # Left pointer (smaller element)
            k = n - 1      # Right pointer (larger element)
            
            # Step 4: Two-pointer movement to count valid (j, k) pairs
            while j < k:
                current_sum = arr[i] + arr[j] + arr[k]
                
                if current_sum < sum:
                    # Key Insight:
                    # Since array is sorted, if arr[i] + arr[j] + arr[k] < sum,
                    # then for the same j, all elements from j+1 to k-1 will also form
                    # a valid triplet with i and j (because they are smaller than arr[k])
                    # So we can count (k - j) triplets at once!
                    count += k - j
                    j += 1  # Move j forward to try larger sums
                else:
                    # Sum is too large → need smaller sum → reduce k
                    k -= 1
        
        # Step 5: Return total count of valid triplets
        return count