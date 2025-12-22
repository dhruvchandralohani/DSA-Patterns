"""
Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without duplicate characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 
Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""
from typing import List

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Find the length of the longest substring without repeating characters.
        Uses sliding window technique with a frequency dictionary.
        """
        n = len(s)
        
        # Step 1: Initialize sliding window variables
        l = 0                    # Left pointer of the current window
        freq = {}                # Frequency map: tracks count of characters in current window
        res = 0                  # Maximum length of substring without repeating chars
        
        # Step 2: Expand the window using right pointer
        for r in range(n):
            ch = s[r]
            
            if ch not in freq:
                # Step 2.1: New character → simply add it
                freq[ch] = 1
            else:
                # Step 2.2: Character already exists → duplicate found
                # Shrink window from left until the duplicate is removed
                while freq[ch] > 0:
                    freq[s[l]] -= 1   # Remove left character from count
                    l += 1           # Move left pointer right
                
                # Optional: clean up zero-count entry (not strictly needed here)
                # del freq[ch]  # This line is unnecessary since we re-add below
                
                # Re-add the current character (now count = 1)
                freq[ch] = 1
            
            # Step 3: Update the maximum length
            # Current window [l, r] has all unique characters
            res = max(res, r - l + 1)
        
        # Step 4: Return the longest substring length found
        return res