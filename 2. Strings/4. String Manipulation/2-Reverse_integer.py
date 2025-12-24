"""
Reverse Integer

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:

Input: x = 123
Output: 321

Example 2:

Input: x = -123
Output: -321

Example 3:

Input: x = 120
Output: 21

Constraints:

-231 <= x <= 231 - 1
"""
class Solution:
    def reverse(self, x: int) -> int:
        """
        Reverse the digits of an integer x.
        - Preserve the sign (positive or negative).
        - Return 0 if the reversed integer overflows 32-bit signed integer range
          [-2^31, 2^31 - 1].
        """
        # Step 1: Convert integer to string for easy digit manipulation
        s = str(x)
        n = len(s)
        res = ""          # String to build the reversed number
        i = n - 1         # Index starting from the last character
        
        # Step 2: Handle negative numbers separately to preserve the '-' sign
        if s[0] == '-':
            # Add the negative sign first
            res += '-'
            
            # Reverse only the digits (skip the '-' sign)
            # Start from last digit (i = n-1) and go until after the first digit (i > 0)
            while i > 0:
                res += s[i]
                i -= 1
        else:
            # Positive number: reverse all digits including the first one
            while i >= 0:
                res += s[i]
                i -= 1
        
        # Step 3: Convert the reversed string back to integer
        res = int(res)
        
        # Step 4: Check for 32-bit signed integer overflow
        # Bounds: -2^31 <= x <= 2^31 - 1
        if res > (2**31) - 1 or res < - (2**31):
            return 0
        
        # Step 5: Return the valid reversed integer
        return res