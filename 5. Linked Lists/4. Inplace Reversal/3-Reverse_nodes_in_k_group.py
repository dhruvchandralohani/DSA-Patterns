"""
Reverse Nodes in k-Group

Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

Example 1:

Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]

Example 2:

Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
 
Constraints:

The number of nodes in the list is n.
1 <= k <= n <= 5000
0 <= Node.val <= 1000
 
Follow-up: Can you solve the problem in O(1) extra memory space?
"""
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Reverse every k nodes in the linked list.
        If the number of remaining nodes < k, leave them as is.
        Do it in-place with O(1) extra space.
        """
        # Step 1: Handle trivial cases
        # - Empty list or k=1 → no reversal needed
        if not head or k == 1:
            return head
        
        # Step 2: Create a dummy node to simplify edge cases (especially when head is part of reversal)
        dummy = ListNode(0)
        dummy.next = head
        
        # Step 3: Initialize pointers
        prev = dummy      # Points to the node BEFORE the current group of k nodes
        curr = head       # Points to the first node of the current group
        
        # Step 4: Count total number of nodes in the list
        # We need this to know how many full groups of k we can reverse
        count = 0
        while curr:
            count += 1
            curr = curr.next
        
        # Step 5: Reset curr to head for actual reversal
        curr = head
        
        # Step 6: Process groups of k nodes while we have enough nodes left
        while count >= k:
            # Save pointers for the current group
            curr = prev.next      # First node of current group
            nxt = curr.next       # Second node (will be used to move nodes)
            
            # Step 6.1: Reverse the links for (k-1) pairs (we reverse k-1 connections)
            for _ in range(1, k):
                # Move the next node (nxt) to the front of the group
                curr.next = nxt.next      # Skip nxt temporarily
                nxt.next = prev.next      # Insert nxt right after prev
                prev.next = nxt           # Update prev's next to new front
                nxt = curr.next           # nxt now points to the new "next" node to move
            
            # Step 6.2: Move prev and count forward for the next group
            prev = curr                   # prev now points to the last node of reversed group
            count -= k                    # We processed k nodes
        
        # Step 7: Return the new head (skip dummy node)
        return dummy.next