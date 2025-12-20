"""
Linked List Cycle II

Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

Do not modify the linked list.

Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Example 2:

Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.

Example 3:

Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.
 
Constraints:

The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.

Follow up: Can you solve it using O(1) (i.e. constant) memory?
"""
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Detect the starting node of a cycle in a singly-linked list (if exists).
        Returns the node where the cycle begins, or None if no cycle.
        Uses Floyd's Cycle Detection (Tortoise and Hare) algorithm.
        """
        # Step 1: Initialize two pointers (slow and fast) at the head
        slow = fast = head
        
        # Step 2: Phase 1 - Detect if a cycle exists
        # Move slow one step, fast two steps until they meet or fast reaches end
        while fast and fast.next:
            slow = slow.next          # Tortoise: 1 step
            fast = fast.next.next     # Hare: 2 steps
            
            if slow == fast:          # Meeting point inside the cycle (if any)
                break                 # Cycle detected → exit loop early
        
        # Step 3: Check if we exited because of no cycle
        # If slow != fast → fast reached end → no cycle
        if slow != fast:
            return None
        
        # Step 4: Phase 2 - Find the start of the cycle
        # Reset slow to head; keep fast at meeting point
        # Both now move one step at a time → they meet at cycle entrance
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        
        # Step 5: slow (and fast) now point to the cycle's starting node
        return slow