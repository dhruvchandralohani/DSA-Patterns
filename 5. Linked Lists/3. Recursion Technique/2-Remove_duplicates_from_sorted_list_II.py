"""
Remove Duplicates from Sorted List II

Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

Example 1:

Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]

Example 2:

Input: head = [1,1,1,2,3]
Output: [2,3]

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
        Remove ALL duplicate nodes from a sorted singly-linked list.
        Only keep nodes that appear exactly once.
        
        Example:
        1 → 2 → 2 → 3 → 3 → 3 → 4 → 5 → 5 → None
        → becomes
        1 → 4 → None
        
        Approach:
        - Use a dummy node to handle edge cases (e.g., duplicates at head)
        - prev: points to the last node that is confirmed to be kept
        - cur: traverses the list
        - When duplicates are found, skip the entire group
        """
        # Step 1: Create dummy node to simplify handling of duplicates at the head
        dummy = ListNode(-1)   # Sentinel value that won't appear in input
        dummy.next = head
        
        # Step 2: Initialize pointers
        prev = dummy           # prev is the last node we know should be kept
        cur = head             # cur traverses the list
        
        # Step 3: Traverse the list
        while cur and cur.next:
            if cur.val == cur.next.val:
                # Step 3.1: Duplicate found → skip all nodes with this value
                # Move cur forward until we pass all duplicates
                while cur.next and cur.val == cur.next.val:
                    cur = cur.next
                
                # Now cur is at the last duplicate
                # Skip the entire duplicate group by linking prev to the node after cur
                prev.next = cur.next
                
                # Do NOT move prev forward — because we haven't confirmed the next node yet
            else:
                # Step 3.2: No duplicate → safe to keep current node
                # Move prev forward (now prev points to cur)
                prev = prev.next
            
            # Always move cur forward for next iteration
            cur = cur.next
        
        # Step 4: Return the head of the cleaned list (skip dummy)
        return dummy.next