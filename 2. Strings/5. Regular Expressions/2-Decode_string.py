"""
Decode String

Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"

Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"

Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"

Constraints:

1 <= s.length <= 30
s consists of lowercase English letters, digits, and square brackets '[]'.
s is guaranteed to be a valid input.
All the integers in s are in the range [1, 300].
"""
class Solution:
    def decodeString(self, s: str) -> str:
        """
        Decode an encoded string where:
        - Numbers in brackets indicate repetition: e.g., "3[a]" → "aaa"
        - Nested brackets are allowed: e.g., "3[a2[c]]" → "accaccacc"
        
        Approach: Use a stack to handle nested brackets.
        - When we encounter '[', push current string and current number onto stack.
        - When we encounter ']', pop number and previous string, repeat current string, and append.
        """
        stack = []           # Stack to store previous strings and numbers during nesting
        curNum = 0           # Current number being built (can be multi-digit)
        curString = ''       # Current string being built inside the current bracket level
        
        # Step 1: Iterate through each character in the input string
        for c in s:
            if c == '[':
                # Step 1.1: Opening bracket → start a new level
                # Save the current state before entering the new bracket
                stack.append(curString)   # Save the string built so far
                stack.append(curNum)      # Save the number for repetition
                # Reset for the new nested level
                curString = ''
                curNum = 0
                
            elif c == ']':
                # Step 1.2: Closing bracket → finish current level
                # Pop the number (how many times to repeat)
                num = stack.pop()
                # Pop the string that was before this bracket
                prevString = stack.pop()
                # Repeat the current string 'num' times and append to previous string
                curString = prevString + num * curString
                
            elif c.isdigit():
                # Step 1.3: Digit → part of a multi-digit number
                # Build the number: e.g., "10" → first '1' → curNum=1, then '0' → curNum=10
                curNum = curNum * 10 + int(c)
                
            else:
                # Step 1.4: Normal letter → just append to current string
                curString += c
        
        # Step 2: After processing all characters, curString holds the final decoded result
        return curString