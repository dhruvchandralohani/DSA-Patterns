"""
First Unique Character in a String

Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Example 1:

Input: s = "leetcode"

Output: 0

Explanation:

The character 'l' at index 0 is the first character that does not occur at any other index.

Example 2:

Input: s = "loveleetcode"

Output: 2

Example 3:

Input: s = "aabb"

Output: -1

Constraints:

1 <= s.length <= 105
s consists of only lowercase English letters.
"""
class Solution:
    def firstUniqChar(self, s: str) -> int:
        """
        Find the index of the first character in string `s` that appears exactly once.
        If no such character exists, return -1.
        
        Approach:
        1. Count the frequency of each character using a dictionary.
        2. Iterate through the string again (with indices) and return the index
           of the first character whose frequency is 1.
        """
        
        # Step 1: Build a frequency dictionary
        # dicts will map each character to its count in the string
        dicts = {}
        for ch in s:
            # If ch is already in dicts, increment its count; otherwise start at 1
            dicts[ch] = dicts.get(ch, 0) + 1
        
        # Step 2: Find the first unique character by checking order of appearance
        # We use enumerate to get both index (i) and character (ch) while preserving original order
        for i, ch in enumerate(s):
            if dicts[ch] == 1:      # This character appears only once in the entire string
                return i           # Return its earliest (first) index
        
        # If we finish the loop without finding any unique character
        return -1