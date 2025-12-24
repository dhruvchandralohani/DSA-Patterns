"""
Find the Index of the First Occurrence in a String

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.

Constraints:

1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.
"""
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        Return the index of the first occurrence of needle in haystack,
        or -1 if needle is not part of haystack.
        
        This is a straightforward implementation of substring search
        using Python's string slicing.
        """
        # Step 1: Handle the edge case where needle is an empty string
        # According to the problem statement, empty needle should return 0
        # (Note: the code below implicitly handles this because range(..., +1) includes the last position)
        # But we don't need special handling here due to the loop bounds.
        
        # Step 2: Determine the maximum starting index we can check
        # We can only start up to len(haystack) - len(needle) inclusive
        # Adding +1 ensures we include the last possible valid starting position
        for i in range(len(haystack) - len(needle) + 1):
            # Step 3: Extract the substring of haystack starting at index i
            # with the same length as needle
            # Compare it directly with needle
            if haystack[i:i + len(needle)] == needle:
                # Step 4: If they match, return the current starting index i
                return i
        
        # Step 5: If no match is found after checking all possible positions,
        # return -1 indicating needle is not present
        return -1