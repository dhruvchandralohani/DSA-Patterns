"""
Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 
Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
"""
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Add two numbers represented as reversed singly-linked lists.
        Each node contains a single digit. Return the sum as a linked list (also reversed).
        """
        # Step 1: Create a dummy node to simplify edge cases
        # The real result will start from dummy.next
        node = ListNode()      # Current working node (starts as dummy)
        res = node             # Save reference to dummy for final return
        
        total = carry = 0      # total: current digit sum + carry, carry: overflow to next digit
        
        # Step 2: Continue while there are digits left in either list or a remaining carry
        while l1 or l2 or carry:
            total = carry      # Start with any carry from previous addition
            
            # Step 2.1: Add digit from l1 if available
            if l1:
                total += l1.val
                l1 = l1.next   # Move to next digit in l1
            
            # Step 2.2: Add digit from l2 if available
            if l2:
                total += l2.val
                l2 = l2.next   # Move to next digit in l2
            
            # Step 2.3: Calculate current digit and new carry
            num = total % 10       # Current digit (0-9)
            carry = total // 10    # Carry over to next position (0 or 1)
            
            # Step 2.4: Create new node with current digit and advance pointer
            node.next = ListNode(num)
            node = node.next       # Move working pointer forward
        
        # Step 3: Return the actual result list (skip the dummy node)
        return res.next