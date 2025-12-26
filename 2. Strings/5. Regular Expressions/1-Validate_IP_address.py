"""
Validate IP Address

Given a string queryIP, return "IPv4" if IP is a valid IPv4 address, "IPv6" if IP is a valid IPv6 address or "Neither" if IP is not a correct IP of any type.

A valid IPv4 address is an IP in the form "x1.x2.x3.x4" where 0 <= xi <= 255 and xi cannot contain leading zeros. For example, "192.168.1.1" and "192.168.1.0" are valid IPv4 addresses while "192.168.01.1", "192.168.1.00", and "192.168@1.1" are invalid IPv4 addresses.

A valid IPv6 address is an IP in the form "x1:x2:x3:x4:x5:x6:x7:x8" where:

1 <= xi.length <= 4
xi is a hexadecimal string which may contain digits, lowercase English letter ('a' to 'f') and upper-case English letters ('A' to 'F').
Leading zeros are allowed in xi.
For example, "2001:0db8:85a3:0000:0000:8a2e:0370:7334" and "2001:db8:85a3:0:0:8A2E:0370:7334" are valid IPv6 addresses, while "2001:0db8:85a3::8A2E:037j:7334" and "02001:0db8:85a3:0000:0000:8a2e:0370:7334" are invalid IPv6 addresses.

Example 1:

Input: queryIP = "172.16.254.1"
Output: "IPv4"
Explanation: This is a valid IPv4 address, return "IPv4".

Example 2:

Input: queryIP = "2001:0db8:85a3:0:0:8A2E:0370:7334"
Output: "IPv6"
Explanation: This is a valid IPv6 address, return "IPv6".

Example 3:

Input: queryIP = "256.256.256.256"
Output: "Neither"
Explanation: This is neither a IPv4 address nor a IPv6 address.

Constraints:

queryIP consists only of English letters, digits and the characters '.' and ':'.
"""
class Solution(object):
    def validIPAddress(self, queryIP):
        """
        Determine if the given string is a valid IPv4, IPv6, or neither.
        
        Workflow:
        1. Check for IPv4 first (exactly 3 dots)
        2. If not IPv4, check for IPv6 (exactly 7 colons)
        3. If neither matches the format, return "Neither"
        """
        
        # ───────────────────────────────
        # Step 1: Check if it could be IPv4 (must have exactly 3 dots)
        # ───────────────────────────────
        if queryIP.count('.') == 3:
            parts = queryIP.split('.')   # Split into 4 parts
            
            # Step 1.1: Validate each of the 4 parts using all()
            # all() returns True only if EVERY condition inside is True
            # Conditions for a valid IPv4 part:
            # - p.isdigit(): must consist only of digits
            # - 0 <= int(p) <= 255: value in valid range
            # - str(int(p)) == p: no leading zeros (e.g., "01" or "001" invalid, "0" valid)
            if all(
                p.isdigit() and 
                0 <= int(p) <= 255 and 
                str(int(p)) == p 
                for p in parts
            ):
                return "IPv4"
        
        # ───────────────────────────────
        # Step 2: Check if it could be IPv6 (must have exactly 7 colons)
        # ───────────────────────────────
        elif queryIP.count(':') == 7:
            parts = queryIP.split(':')   # Split into 8 parts
            
            # Step 2.1: Validate each of the 8 parts using all()
            # Conditions for a valid IPv6 part:
            # - 1 <= len(p) <= 4: each group must have 1 to 4 hex digits
            # - all(c in "0123456789abcdefABCDEF" for c in p): every character must be valid hex
            if all(
                1 <= len(p) <= 4 and 
                all(c in "0123456789abcdefABCDEF" for c in p)
                for p in parts
            ):
                return "IPv6"
        
        # Step 3: If neither IPv4 nor IPv6 format matches → invalid
        return "Neither"