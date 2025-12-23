"""
Maximum Number of Balloons

Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.

Example 1:

Input: text = "nlaebolko"
Output: 1

Example 2:

Input: text = "loonbalxballpoon"
Output: 2

Example 3:

Input: text = "leetcode"
Output: 0
 
Constraints:

1 <= text.length <= 104
text consists of lower case English letters only.
"""
from collections import Counter
from typing import List

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        """
        Return the maximum number of times the word "balloon" can be formed
        using the characters from the given string `text`.
        
        Each "balloon" requires:
            'b': 1
            'a': 1
            'l': 2
            'o': 2
            'n': 1
        """
        # Step 1: Count the frequency of each character in the input string
        # Counter creates a dictionary-like object: char → count
        c = Counter(text)
        
        # Step 2: Determine how many "balloon" instances we can form
        # We are limited by the scarcest required character (considering multiplicity)
        # - 'b', 'a', 'n' appear once → use their count directly
        # - 'l' and 'o' appear twice → we can only use floor(count / 2)
        return min(
            c['b'],          # number of 'b's available
            c['a'],          # number of 'a's available
            c['l'] // 2,     # number of pairs of 'l's (since we need 2 per balloon)
            c['o'] // 2,     # number of pairs of 'o's
            c['n']           # number of 'n's available
        )
        
        # Note: If a required character is missing, Counter returns 0 for it,
        # so min() will correctly return 0 in that case.