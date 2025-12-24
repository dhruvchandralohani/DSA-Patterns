"""
String to Integer (atoi)

Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

The algorithm for myAtoi(string s) is as follows:

Whitespace: Ignore any leading whitespace (" ").
Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity if neither present.
Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the integer to remain in the range. Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.
Return the integer as the final result.

Example 1:

Input: s = "42"

Output: 42

Explanation:

The underlined characters are what is read in and the caret is the current reader position.
Step 1: "42" (no characters read because there is no leading whitespace)
         ^
Step 2: "42" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "42" ("42" is read in)
           ^
Example 2:

Input: s = " -042"

Output: -42

Explanation:

Step 1: "   -042" (leading whitespace is read and ignored)
            ^
Step 2: "   -042" ('-' is read, so the result should be negative)
             ^
Step 3: "   -042" ("042" is read in, leading zeros ignored in the result)
               ^
Example 3:

Input: s = "1337c0d3"

Output: 1337

Explanation:

Step 1: "1337c0d3" (no characters read because there is no leading whitespace)
         ^
Step 2: "1337c0d3" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "1337c0d3" ("1337" is read in; reading stops because the next character is a non-digit)
             ^
Example 4:

Input: s = "0-1"

Output: 0

Explanation:

Step 1: "0-1" (no characters read because there is no leading whitespace)
         ^
Step 2: "0-1" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "0-1" ("0" is read in; reading stops because the next character is a non-digit)
          ^
Example 5:

Input: s = "words and 987"

Output: 0

Explanation:

Reading stops at the first non-digit character 'w'.

Constraints:

0 <= s.length <= 200
s consists of English letters (lower-case and upper-case), digits (0-9), ' ', '+', '-', and '.'.
"""
class Solution:
    def myAtoi(self, s: str) -> int:
        """
        Convert a string to a 32-bit signed integer (similar to C's atoi).
        Rules:
        - Ignore leading whitespace
        - Optional '+' or '-' sign
        - Read digits until non-digit character
        - Ignore rest of string
        - Clamp result to [-2^31, 2^31 - 1] if overflow
        - Return 0 for empty or invalid input
        """
        # Step 1: Remove leading and trailing whitespace
        s = s.strip()
        
        # Step 2: Handle empty string after stripping
        if not s:
            return 0
        
        # Step 3: Determine sign and move index past sign character
        sign = 1          # Default to positive
        i = 0             # Index for traversing the string
        res = 0           # Accumulated result
        
        if s[0] == '-':
            sign = -1     # Negative number
            i += 1        # Skip the '-' sign
        elif s[0] == '+':
            i += 1        # Skip the '+' sign (sign remains positive)
        
        # Step 4: Process digits one by one
        while i < len(s) and s[i].isdigit():
            # Build the number: shift left by one digit and add current
            res = res * 10 + int(s[i])
            
            # Step 5: Check for overflow on every step
            # Apply sign temporarily to check bounds
            if sign * res > 2**31 - 1:      # Overflow positive side
                return 2**31 - 1           # Return INT_MAX
            if sign * res < -2**31:         # Overflow negative side
                return -2**31              # Return INT_MIN
            
            i += 1
        
        # Step 6: Apply sign and return the final result
        return sign * res