"""
Middle of the Linked List

Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

Example 1:

Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.
Example 2:

Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
 
Constraints:

The number of nodes in the list is in the range [1, 100].
1 <= Node.val <= 100
"""
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Return the middle node of a singly-linked list.
        If there are two middle nodes (even length), return the second one.
        """
        # Step 1: Initialize two pointers
        # slow: moves one step at a time
        # fast: moves two steps at a time
        # Both start at the head
        slow = fast = head
        
        # Step 2: Traverse the list with the fast pointer
        # Continue as long as fast can take full two steps (fast and fast.next exist)
        while fast and fast.next:
            # Move slow one step forward
            slow = slow.next
            
            # Move fast two steps forward
            fast = fast.next.next
        
        # Step 3: When fast reaches the end:
        # - slow will be exactly at the middle node
        # For odd length:  fast ends at last node → loop stops
        # For even length: fast ends just past the last node → loop stops after slow reaches second middle
        return slow