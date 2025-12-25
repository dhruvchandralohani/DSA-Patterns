"""
Reverse Linked List

Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:

Input: head = [1,2]
Output: [2,1]

Example 3:

Input: head = []
Output: []
 
Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000 

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
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
        Reverse a singly-linked list in-place and return the new head.
        
        Iterative approach using three pointers:
        - prevN: points to the already reversed portion (initially None)
        - currN: current node being processed
        - nextN: temporary storage for the next node (to avoid losing it after changing links)
        """
        # Step 1: Handle base cases
        # - Empty list (None) or single node → already "reversed"
        if not head or not head.next:
            return head
        
        # Step 2: Initialize pointers
        currN = head    # Start with the original head
        prevN = None    # Reversed portion is empty at the beginning
        nextN = None    # Will hold the next node temporarily
        
        # Step 3: Traverse the list and reverse links one by one
        while currN:
            # Save the next node before we overwrite currN.next
            nextN = currN.next
            
            # Reverse the link: point current node backward to prevN
            currN.next = prevN
            
            # Move pointers forward
            prevN = currN       # prevN now includes the current node
            currN = nextN       # Move to the next unreversed node
        
        # Step 4: prevN now points to the last node processed → new head of reversed list
        head = prevN
        
        # Step 5: Return the new head
        return head