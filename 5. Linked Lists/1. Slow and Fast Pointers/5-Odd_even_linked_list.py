"""
Odd Even Linked List

Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.

Example 1:

Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]
Example 2:

Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]
 
Constraints:

The number of nodes in the linked list is in the range [0, 104].
-106 <= Node.val <= 106
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