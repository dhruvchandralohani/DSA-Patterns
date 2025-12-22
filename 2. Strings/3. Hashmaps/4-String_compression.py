"""
String Compression

Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

You must write an algorithm that uses only constant extra space.

Note: The characters in the array beyond the returned length do not matter and should be ignored. 

Example 1:

Input: chars = ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".

Example 2:

Input: chars = ["a"]
Output: Return 1, and the first character of the input array should be: ["a"]
Explanation: The only group is "a", which remains uncompressed since it's a single character.

Example 3:

Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".

Constraints:

1 <= chars.length <= 2000
chars[i] is a lowercase English letter, uppercase English letter, digit, or symbol.
"""
from typing import List  # If needed for type hints

class Solution:
    def compress(self, chars: List[str]) -> int:
        """
        Compresses the input list of characters using the run-length encoding rule:
        - Groups of repeated characters are replaced by the character followed by the count (if count > 1).
        - Modification is done in-place.
        
        Returns the length of the compressed array.
        
        Example:
            ["a","a","b","b","c","c","c"] → ["a","2","b","2","c","3"] → returns 6
        """
        
        # `write` is the position where we write the next character/digit in the compressed result
        # We modify chars in-place, starting from index 0
        write = 0
        
        # `i` is the pointer that scans through the original array
        i = 0
        
        # Length of the input array
        n = len(chars)
        
        # Main loop: process groups of identical characters
        while i < n:
            # Current character we're processing
            current = chars[i]
            
            # Count how many times it appears consecutively
            count = 0
            while i < n and chars[i] == current:
                i += 1          # Move the read pointer forward
                count += 1      # Increment the run length
            
            # Step 1: Write the character itself
            chars[write] = current
            write += 1
            
            # Step 2: If the count is greater than 1, write the count as digits
            # (If count == 1, we only write the character, as per the rule)
            if count > 1:
                # Convert count to string (e.g., 12 → "12")
                for digit in str(count):
                    chars[write] = digit   # Write each digit one by one
                    write += 1
            
        # After processing all groups, `write` equals the new length of the compressed array
        return write