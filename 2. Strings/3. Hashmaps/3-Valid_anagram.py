"""
Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 
Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Check if strings `s` and `t` are anagrams of each other.
        An anagram is a word or phrase formed by rearranging the letters of another,
        using all the original letters exactly once.
        
        Returns True if `t` is an anagram of `s`, False otherwise.
        """
        
        # Step 1: Create frequency counters (dictionaries) for both strings
        dictn1 = {}  # Will store character counts for string `s`
        dictn2 = {}  # Will store character counts for string `t`
        
        # Step 2: Count characters in string `s`
        for ch in s:
            # Increment count for ch in dictn1
            # If ch not present, dictn1.get(ch, 0) returns 0, then +1 → starts at 1
            dictn1[ch] = dictn1.get(ch, 0) + 1
        
        # Step 3: Count characters in string `t`
        for ch in t:
            # Same logic: increment count for each character in `t`
            dictn2[ch] = dictn2.get(ch, 0) + 1
        
        # Step 4: Compare the two frequency dictionaries
        # If they are identical (same keys with same counts), the strings are anagrams
        return dictn1 == dictn2