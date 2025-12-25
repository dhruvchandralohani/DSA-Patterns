"""
Reorder List

You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Example 1:

Input: head = [1,2,3,4]
Output: [1,4,2,3]

Example 2:

Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]

Constraints:

The number of nodes in the list is in the range [1, 5 * 104].
1 <= Node.val <= 1000
"""
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Helper function to reverse a linked list and return the new head.
        Used to reverse the second half in reorderList.
        """
        prev = None    # Points to the reversed portion (starts empty)
        cur = head     # Current node being processed
        
        # Step 1: Reverse links one by one
        while cur:
            temp = cur.next        # Save next node
            cur.next = prev        # Point current node backward
            prev = cur             # Move prev to current
            cur = temp             # Move to next node
        
        # Step 2: Return new head (last node processed)
        return prev
    
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Reorder the linked list in-place: L0→Ln→L1→Ln-1→L2→Ln-2→...
        Example: 1→2→3→4 becomes 1→4→2→3
        
        Approach:
        - Find the middle using slow/fast pointers
        - Split into two halves
        - Reverse the second half
        - Merge the two halves alternately
        """
        # Step 1: Handle trivial cases (empty or single node)
        # Implicitly handled since slow/fast will work fine, but no explicit check needed
        
        # Step 2: Find the middle of the list using slow and fast pointers
        # - slow will end up at the middle (or just before for even length)
        # - fast moves twice as fast to reach the end
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 3: Split the list into two halves
        # - second points to the start of the second half
        # - Set slow.next = None to end the first half
        second = slow.next
        slow.next = None
        
        # Step 4: Reverse the second half
        # - Call helper function to reverse from second
        rev = self.reverseList(second)
        
        # Step 5: Merge the two halves alternately
        # - first points to original list (first half)
        # - second points to reversed second half
        first = head
        second = rev
        
        # Step 6: Interleave nodes
        while second:
            # Save next pointers to avoid losing them
            temp1 = first.next    # Next node in first half
            temp2 = second.next   # Next node in second half
            
            # Link first node to second node
            first.next = second
            # Link second node to next node in first half
            second.next = temp1
            
            # Move pointers forward
            first = temp1
            second = temp2