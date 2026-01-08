"""
Find Smallest Letter Greater Than Target

You are given an array of characters letters that is sorted in non-decreasing order, and a character target. There are at least two different characters in letters.

Return the smallest character in letters that is lexicographically greater than target. If such a character does not exist, return the first character in letters.

Example 1:

Input: letters = ["c","f","j"], target = "a"
Output: "c"
Explanation: The smallest character that is lexicographically greater than 'a' in letters is 'c'.

Example 2:

Input: letters = ["c","f","j"], target = "c"
Output: "f"
Explanation: The smallest character that is lexicographically greater than 'c' in letters is 'f'.

Example 3:

Input: letters = ["x","x","y","y"], target = "z"
Output: "x"
Explanation: There are no characters in letters that is lexicographically greater than 'z' so we return letters[0].

Constraints:

2 <= letters.length <= 104
letters[i] is a lowercase English letter.
letters is sorted in non-decreasing order.
letters contains at least two different characters.
target is a lowercase English letter.
"""
from typing import List

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # Number of characters in the sorted list
        n = len(letters)

        # Left and right pointers for binary search
        l = 0
        r = n - 1

        # Position of the smallest letter greater than target
        # Initialized to 0 to handle the wrap-around case
        pos = 0

        # Binary search to find the first letter greater than target
        while l <= r:
            # Calculate the middle index
            mid = (l + r) // 2

            # If current letter is strictly greater than target,
            # it is a valid candidate
            if letters[mid] > target:
                pos = mid          # Store current best answer
                r = mid - 1        # Try to find a smaller index on the left

            # Otherwise, move to the right half
            else:
                l = mid + 1

        # Return the letter at the stored position
        # If no letter > target exists, pos remains 0 (wrap-around)
        return letters[pos]
