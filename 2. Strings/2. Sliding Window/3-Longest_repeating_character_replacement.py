"""
Longest Repeating Character Replacement

You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations. 

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too. 

Constraints:

1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length
"""
class Solution(object):
    def characterReplacement(self, s, k):
        """
        Find the length of the longest substring where you can replace at most k characters
        to make all characters in the substring the same.
        
        Sliding window technique: maintain a window [l, r] where the number of replacements needed
        (window length - count of the most frequent character) <= k.
        """
        max_count = 0          # Tracks the maximum frequency of any single character in current window
        l = 0                  # Left pointer of the sliding window
        freq = {}              # Frequency map of characters in current window [l, r]
        n = len(s)             # Length of the string
        
        # Step 1: Expand the window with right pointer
        for r in range(n):
            # Add current character to the window
            freq[s[r]] = freq.get(s[r], 0) + 1
            
            # Update the highest frequency seen in the current window
            max_count = max(max_count, freq[s[r]])
            
            # Step 2: Check if current window is valid
            # Replacements needed = (window length) - (most frequent char count)
            # If replacements needed > k → window is too large → shrink from left
            if r - l + 1 - max_count > k:
                # Remove the leftmost character
                freq[s[l]] -= 1
                l += 1  # Shrink window from left
            
            # Note: We don't update max_count when shrinking because:
            # - The new max could be smaller, but keeping the old (larger) max_count
            #   allows the window to potentially grow larger later.
            # - This is a valid optimization — we only care about feasibility, not exact max.
        
        # Step 3: After the loop, the largest valid window is [l, n-1]
        # Its length is n - l
        return n - l