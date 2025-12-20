"""
Merge Two Sorted Lists

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:

Input: list1 = [], list2 = []
Output: []

Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
 
Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Merge two sorted singly-linked lists into one sorted list.
        The merged list should be made by splicing together the nodes of the two lists.
        """
        # Step 1: Create a dummy node to simplify edge cases (e.g., empty lists)
        # The real merged list will start from dummy.next
        head = ListNode(-1)   # Dummy node with sentinel value (-1)
        l = head              # Working pointer that builds the merged list
        
        l1 = list1            # Pointer for traversing list1
        l2 = list2            # Pointer for traversing list2
        
        # Step 2: Merge while both lists have remaining nodes
        # Compare current nodes and attach the smaller one to the result
        while l1 and l2:
            if l1.val < l2.val:
                # list1 has smaller value → attach l1 node
                l.next = l1
                l = l.next        # Move working pointer forward
                l1 = l1.next      # Advance in list1
            else:
                # list2 has smaller or equal value → attach l2 node
                l.next = l2
                l = l.next        # Move working pointer forward
                l2 = l2.next      # Advance in list2
        
        # Step 3: Append remaining nodes from the non-empty list
        # At most one of these will execute
        if l1:
            l.next = l1           # Attach leftover nodes from list1
        if l2:
            l.next = l2           # Attach leftover nodes from list2
        
        # Step 4: Return the merged list (skip the dummy node)
        return head.next