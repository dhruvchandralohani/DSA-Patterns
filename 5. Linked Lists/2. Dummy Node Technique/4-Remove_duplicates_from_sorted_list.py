"""
Remove Duplicates from Sorted List

Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.
 
Example 1:

Input: head = [1,1,2]
Output: [1,2]
Example 2:

Input: head = [1,1,2,3,3]
Output: [1,2,3]
 
Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
"""
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Remove all duplicate values from a sorted singly-linked list.
        The list is guaranteed to be sorted in ascending order.
        Modify the list in-place and return the head of the updated list.
        """
        # Step 1: Store the original head to return at the end
        # We will modify pointers, but the first node always stays valid
        res = head
        
        # Step 2: Traverse the list while there are at least two nodes
        while head and head.next:
            if head.val == head.next.val:
                # Step 2.1: Duplicate found
                # Skip the duplicate node by linking current node directly to the one after next
                # Key line: head.next = head.next.next
                # This effectively removes head.next from the list
                head.next = head.next.next
                # Note: we do NOT move head forward here
                # Because the new head.next might also be a duplicate
            else:
                # Step 2.2: No duplicate → safe to move to next node
                head = head.next
        
        # Step 3: Return the head of the deduplicated list
        return res