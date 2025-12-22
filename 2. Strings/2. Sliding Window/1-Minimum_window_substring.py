"""
Minimum Window Substring

Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.

Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters. 

Follow up: Could you find an algorithm that runs in O(m + n) time?
"""
from typing import Dict

class Solution:
    def check(self, str1: Dict[str, int], str2: Dict[str, int]) -> bool:
        """
        Helper function: Check if frequency map str1 contains at least the counts in str2.
        i.e., for every character in str2, str1 must have equal or higher count.
        """
        for key, value in str2.items():
            if key not in str1 or str1[key] < value:
                return False
        return True
    
    def minWindow(self, s: str, t: str) -> str:
        """
        Find the minimum length window substring in s that contains all characters from t
        (including duplicates). Return the substring itself. If no such window exists, return "".
        
        Sliding window technique:
        - Expand right pointer to include characters
        - When window satisfies condition, shrink from left to minimize
        """
        str1, str2 = {}, {}      # str1: frequency in current window, str2: required from t
        n = len(s)
        
        # Step 1: Build frequency map for string t (required characters)
        for i in range(len(t)):
            str2[t[i]] = str2.get(t[i], 0) + 1
        
        l = 0                    # Left pointer of the sliding window
        res = ""                 # To store the smallest valid window found
        
        # Step 2: Expand window with right pointer
        for r in range(n):
            # Add current character from s to the window frequency
            str1[s[r]] = str1.get(s[r], 0) + 1
            
            # Step 3: While current window contains all required characters
            # Try to shrink from left to make window smaller
            while self.check(str1, str2):
                window = s[l:r+1]   # Current valid substring
                
                # Update result if this is the first or smaller than previous
                if res == "" or len(window) < len(res):
                    res = window
                
                # Shrink window from left
                str1[s[l]] -= 1
                l += 1
        
        # Step 4: Return the smallest valid window found (or "" if none)
        return res