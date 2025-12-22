"""
Longest Substring with K Uniques

You are given a string s consisting only lowercase alphabets and an integer k. Your task is to find the length of the longest substring that contains exactly k distinct characters.

Note : If no such substring exists, return -1. 

Examples:

Input: s = "aabacbebebe", k = 3
Output: 7
Explanation: The longest substring with exactly 3 distinct characters is "cbebebe", which includes 'c', 'b', and 'e'.

Input: s = "aaaa", k = 2
Output: -1
Explanation: There's no substring with 2 distinct characters.

Input: s = "aabaaab", k = 2
Output: 7
Explanation: The entire string "aabaaab" has exactly 2 unique characters 'a' and 'b', making it the longest valid substring.

Constraints:
1 ≤ s.size() ≤ 105
1 ≤ k ≤ 26
"""
class Solution:
    def longestKSubstr(self, s, k):
        """
        Find the length of the longest substring that contains at most k distinct characters.
        Returns -1 if no such substring exists.
        Uses sliding window with a frequency dictionary.
        """
        n = len(s)
        
        # Step 1: Initialize sliding window pointers and frequency map
        l = 0                   # Left pointer of the window
        freq = {}               # Dictionary to track character counts in current window
        res = -1                # Maximum length of valid substring found (-1 if none)
        
        # Step 2: Expand the window using right pointer
        for r in range(n):
            # Add current character to the window
            freq[s[r]] = freq.get(s[r], 0) + 1
            
            # Step 3: Shrink window from left if number of distinct characters > k
            while len(freq) > k:
                # Remove leftmost character
                freq[s[l]] -= 1
                # If count reaches 0, remove the character from dictionary
                if freq[s[l]] == 0:
                    del freq[s[l]]
                l += 1  # Move left pointer right
            
            # Step 4: After shrinking, if we have exactly k distinct characters
            # Update the maximum length
            if len(freq) == k:
                res = max(res, r - l + 1)
        
        # Step 5: Return the longest valid substring length found
        return res