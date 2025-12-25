"""
Reverse Linked List II

Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

Example 1:

Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]

Example 2:

Input: head = [5], left = 1, right = 1
Output: [5] 

Constraints:

The number of nodes in the list is n.
1 <= n <= 500
-500 <= Node.val <= 500
1 <= left <= right <= n

Follow up: Could you do it in one pass?
"""
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        """
        Reverse a sublist of the linked list from position left to right (1-based indexing).
        Do this in-place with O(1) extra space.
        """
        # Step 1: Edge cases - no reversal needed
        if not head or left == right:
            return head
        
        # Step 2: Use a dummy node to simplify handling when reversal starts at head (left=1)
        dummy = ListNode(0, head)
        
        # Step 3: Move 'prev' to the node just BEFORE the sublist to reverse
        # After this loop, prev points to the node at position (left - 1)
        prev = dummy
        for _ in range(left - 1):
            prev = prev.next
        
        # Step 4: 'cur' is the first node of the sublist we will reverse
        cur = prev.next
        
        # Step 5: Perform the reversal of (right - left) nodes
        # We repeatedly take the node after 'cur' and move it to the position right after 'prev'
        # This effectively reverses the links one by one
        for _ in range(right - left):
            # temp holds the node we are about to move
            temp = cur.next
            
            # Disconnect temp from the rest of the list
            cur.next = temp.next
            
            # Insert temp right after prev (becomes new head of reversed part)
            temp.next = prev.next
            prev.next = temp
        
        # Step 6: Return the head of the modified list (dummy.next skips the dummy node)
        return dummy.next