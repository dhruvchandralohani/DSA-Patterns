"""
Find All Anagrams in a String

Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
 
Constraints:

1 <= s.length, p.length <= 3 * 104
s and p consist of lowercase English letters.
"""
from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """
        Find all starting indices of anagrams of string p in string s.
        An anagram is a substring with exactly the same character frequencies as p.
        
        Sliding window technique with frequency dictionaries.
        """
        dicts = {}          # Frequency map for current window in s
        dictp = {}          # Frequency map for string p (target)
        m = len(s)          # Length of string s
        n = len(p)          # Length of string p
        
        # Step 1: Edge case - if p is longer than s, no anagram possible
        if n > m:
            return []
        
        ans = []            # List to store starting indices of valid anagrams
        
        # Step 2: Build frequency map for p
        for ch in p:
            dictp[ch] = dictp.get(ch, 0) + 1
        
        # Step 3: Build initial frequency map for first window s[0:n]
        for i in range(n):
            dicts[s[i]] = dicts.get(s[i], 0) + 1
        
        # Step 4: Slide the window across s
        # We check n windows: [0:n], [1:n+1], ..., [m-n:m]
        for i in range(m - n + 1):
            # Check if current window is an anagram of p
            if dicts == dictp:
                ans.append(i)   # i is the starting index
            
            # If this is not the last window, slide it right by 1
            if i < m - n:
                # Add the new character entering the window
                dicts[s[i + n]] = dicts.get(s[i + n], 0) + 1
                
                # Remove the character leaving the window
                dicts[s[i]] -= 1
                if dicts[s[i]] == 0:
                    del dicts[s[i]]   # Clean up zero-count entry
        
        # Step 5: Return all starting indices of anagrams
        return ans