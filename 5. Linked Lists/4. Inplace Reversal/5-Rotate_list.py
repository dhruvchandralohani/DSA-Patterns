"""
Rotate List

Given the head of a linked list, rotate the list to the right by k places.

Example 1:

Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Example 2:

Input: head = [0,1,2], k = 4
Output: [2,0,1]
 
Constraints:

The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 109
"""
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Rotate the linked list to the right by k places.
        Example: 1→2→3→4→5, k=2 → 4→5→1→2→3
        
        Approach:
        - First, find the length of the list.
        - Effective rotations = k % length (since rotating by full length brings it back)
        - If effective rotations == 0 → no change
        - Otherwise, find the new tail (length - rotations - 1 steps from head),
          break the list there, and connect old tail to old head.
        """
        # Step 1: Handle empty list
        if not head:
            return head
        
        # Step 2: Find the length of the list and get a pointer to the tail
        length = 1
        dummy = head                  # dummy will become the last node (tail)
        while dummy.next:             # Traverse until the end
            dummy = dummy.next
            length += 1
        
        # Step 3: Reduce k to effective rotations (rotating by full length does nothing)
        position = k % length
        
        # Step 4: If effective rotations are 0 → list remains unchanged
        if position == 0:
            return head
        
        # Step 5: Find the node that will become the new tail
        # We need to go (length - position - 1) steps from the head
        current = head
        for _ in range(length - position - 1):
            current = current.next
        
        # Step 6: current is now the new tail
        # current.next will be the new head
        new_head = current.next
        
        # Step 7: Break the link to separate the list into two parts
        current.next = None
        
        # Step 8: Connect the original tail to the original head
        # dummy is still pointing to the old tail
        dummy.next = head
        
        # Step 9: Return the new head
        return new_head