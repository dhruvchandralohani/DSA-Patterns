"""
Remove Nth Node From End of List

Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
 
Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz

Follow up: Could you do this in one pass?
"""
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Remove the n-th node from the end of a singly-linked list and return the new head.
        Uses a dummy node + two-pointer technique (fast and slow) to do it in one pass.
        """
        # Step 1: Create a dummy node pointing to the head
        # This handles edge cases (e.g., removing the head) gracefully
        res = ListNode(0, head)   # dummy.val = 0, dummy.next = original head
        dummy = res               # slow pointer (will lag behind fast pointer)
        
        # Step 2: Move the fast pointer (head) exactly n steps ahead
        # After this loop, head is n nodes ahead of dummy
        for _ in range(n):
            head = head.next      # fast pointer advances n steps
        
        # Step 3: Move both pointers together until fast reaches the end
        # When fast becomes None, dummy will be pointing to the node BEFORE the one to remove
        while head:
            head = head.next      # fast pointer moves forward
            dummy = dummy.next    # slow pointer moves forward (maintains gap of n)
        
        # Step 4: Remove the n-th node from the end
        # dummy.next is the node to delete → skip it by linking to the one after
        dummy.next = dummy.next.next
        
        # Step 5: Return the new head (skip the dummy node)
        return res.next