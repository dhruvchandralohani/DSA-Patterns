"""
Ransom Note

Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true

Constraints:

1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.
"""
from typing import Dict

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        Determine if a ransom note can be constructed from the characters in a magazine.
        Each character in the magazine can only be used once in the ransom note.
        
        Approach: Count frequency of characters in both strings and check if magazine
        has at least as many of each character as required by the ransom note.
        """
        dictRansom: Dict[str, int] = {}   # Frequency map for characters in ransomNote
        dictMaga: Dict[str, int] = {}     # Frequency map for characters in magazine
        
        # Step 1: Count character frequencies in the ransom note
        for ch in ransomNote:
            dictRansom[ch] = dictRansom.get(ch, 0) + 1
        
        # Step 2: Count character frequencies in the magazine
        for ch in magazine:
            dictMaga[ch] = dictMaga.get(ch, 0) + 1
        
        # Step 3: Check if magazine has enough of each character required by ransom note
        for key, value in dictRansom.items():
            # If the character is missing in magazine OR magazine has fewer than needed
            if key not in dictMaga or dictMaga[key] < value:
                return False   # Cannot construct the note
        
        # Step 4: All required characters are available in sufficient quantity
        return True