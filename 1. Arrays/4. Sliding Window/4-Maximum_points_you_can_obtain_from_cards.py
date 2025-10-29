"""
Maximum Points You Can Obtain from Cards

There are several cards arranged in a row, and each card has an associated number of points. The points are given in the integer array cardPoints.

In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.

Your score is the sum of the points of the cards you have taken.

Given the integer array cardPoints and the integer k, return the maximum score you can obtain.

 

Example 1:

Input: cardPoints = [1,2,3,4,5,6,1], k = 3
Output: 12
Explanation: After the first step, your score will always be 1. However, choosing the rightmost card first will maximize your total score. The optimal strategy is to take the three cards on the right, giving a final score of 1 + 6 + 5 = 12.
Example 2:

Input: cardPoints = [2,2,2], k = 2
Output: 4
Explanation: Regardless of which two cards you take, your score will always be 4.
Example 3:

Input: cardPoints = [9,7,7,9,7,7,9], k = 7
Output: 55
Explanation: You have to take all the cards. Your score is the sum of points of all cards.
 

Constraints:

1 <= cardPoints.length <= 105
1 <= cardPoints[i] <= 104
1 <= k <= cardPoints.length
"""
from typing import List

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        """
        Maximize points by taking exactly k cards from the beginning or end.
        Equivalent to: Minimize the sum of (n-k) cards taken from the middle.
        """
        # Step 1: Get array size and total sum
        n = len(cardPoints)
        total_sum = sum(cardPoints)  # Sum of all cards
        
        # Step 2: Handle edge case - taking all cards
        m = n - k  # Number of cards we must leave in the middle (n-k)
        if m == 0:
            return total_sum  # k == n → take all cards
        
        # Step 3: Initialize sliding window of size m
        # We want the minimum sum of any contiguous m cards (the "leftover" middle)
        window_sum = sum(cardPoints[:m])  # First window: indices 0 to m-1
        min_sub = window_sum              # Track minimum middle sum
        
        # Step 4: Slide the window across the array
        # Move window right by adding new element and removing old one
        for i in range(m, n):
            # Expand right: include cardPoints[i]
            # Shrink left: exclude cardPoints[i-m]
            window_sum += cardPoints[i] - cardPoints[i - m]
            
            # Update minimum if current window sum is smaller
            if window_sum < min_sub:
                min_sub = window_sum
        
        # Step 5: Maximize score
        # Total sum minus minimum middle sum = maximum k cards from ends
        return total_sum - min_sub