"""
Valid Perfect Square

Given a positive integer num, return true if num is a perfect square or false otherwise.

A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.

You must not use any built-in library function, such as sqrt.

Example 1:

Input: num = 16
Output: true
Explanation: We return true because 4 * 4 = 16 and 4 is an integer.

Example 2:

Input: num = 14
Output: false
Explanation: We return false because 3.742 * 3.742 = 14 and 3.742 is not an integer.

Constraints:

1 <= num <= 231 - 1
"""
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # Any number less than 2 (0 or 1) is a perfect square
        if num < 2:
            return True

        # Search space for the square root:
        # it must lie between 2 and num // 2
        l = 2
        r = num // 2

        # Binary search to find an integer whose square equals num
        while l <= r:
            # Find the middle candidate
            mid = (l + r) // 2

            # Square the candidate
            res = mid * mid

            # If mid^2 equals num, num is a perfect square
            if res == num:
                return True

            # If mid^2 is smaller than num,
            # search in the right half
            elif res < num:
                l = mid + 1

            # If mid^2 is larger than num,
            # search in the left half
            else:
                r = mid - 1

        # If no integer square root is found, num is not a perfect square
        return False
