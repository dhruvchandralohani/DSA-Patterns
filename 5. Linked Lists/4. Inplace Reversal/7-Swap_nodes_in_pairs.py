"""
Swap Nodes in Pairs

Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

Example 1:

Input: head = [1,2,3,4]

Output: [2,1,4,3]

Example 2:

Input: head = []

Output: []

Example 3:

Input: head = [1]

Output: [1]

Example 4:

Input: head = [1,2,3]

Output: [2,1,3]

Constraints:

The number of nodes in the list is in the range [0, 100].
0 <= Node.val <= 100
"""
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Swap every two adjacent nodes in the linked list and return the new head.
        Example: 1→2→3→4 → 2→1→4→3
        
        Approach: Use a dummy node and iteratively swap pairs.
        """
        # Step 1: Create a dummy node to handle edge cases (especially when head is swapped)
        # dummy.next will always point to the current head of the list
        dummy = ListNode(0, head)
        
        # Step 2: Initialize pointers
        # prev: points to the node BEFORE the current pair (starts at dummy)
        # cur: points to the first node of the current pair to swap
        prev = dummy
        cur = head
        
        # Step 3: Continue while there are at least two nodes left to swap
        while cur and cur.next:
            # Save pointers for the next pair and the second node of current pair
            npn = cur.next.next    # "next pair node" - first node after the current pair
            second = cur.next      # second node in current pair (to become new first)
            
            # Step 3.1: Perform the swaps
            # 1. Second node points to first node (reverse within pair)
            second.next = cur
            
            # 2. First node points to the node after the pair
            cur.next = npn
            
            # 3. Previous node points to the new first node of the pair (second)
            prev.next = second
            
            # Step 3.2: Move pointers forward for the next pair
            # prev now points to the last node of the just-swapped pair (original first node)
            prev = cur
            
            # cur moves to the start of the next pair
            cur = npn
        
        # Step 4: Return the new head (skip the dummy node)
        return dummy.next