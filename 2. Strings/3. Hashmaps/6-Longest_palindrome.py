"""
Longest Palindrome

Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome.

Example 1:

Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

Example 2:

Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.

Constraints:

1 <= s.length <= 2000
s consists of lowercase and/or uppercase English letters only.
"""
class Solution:
    def longestPalindrome(self, s: str) -> int:
        """
        Return the length of the longest palindrome that can be built
        using the characters from string `s` (each character can be used as many times as it appears).
        
        Key Insight:
        - In a palindrome, all characters except possibly one (the center) must have even counts.
        - We can use all even-count characters fully.
        - For odd-count characters, we can use (count - 1) to make them even, and keep one odd as center.
        """
        leng = 0                # Step 1: Will accumulate the total length of the palindrome
        dictn = {}              # Step 2: Frequency map: character → count in s
        
        # Step 3: Count frequency of each character
        for ch in s:
            dictn[ch] = dictn.get(ch, 0) + 1
        
        # Step 4: Process each character's count
        for val in dictn.values():
            if val % 2 == 0:
                # Even count → can use all characters (pair them up)
                leng += val
            else:
                # Odd count → use (val - 1) to make even, leave one out for now
                leng += val - 1
        
        # Step 5: If there is any character with odd count,
        # we can place one of them in the center → add +1 to length
        # Condition: if the total even part is less than original length → means at least one odd count exists
        if len(s) > leng:
            return leng + 1
        else:
            # No odd counts → all even → already maximum length
            return leng