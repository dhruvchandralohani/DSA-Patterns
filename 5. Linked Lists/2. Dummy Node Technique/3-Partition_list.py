"""
Partition List

Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example 1:

Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]

Example 2:

Input: head = [2,1], x = 2
Output: [1,2]
 
Constraints:

The number of nodes in the list is in the range [0, 200].
-100 <= Node.val <= 100
-200 <= x <= 200
"""
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        """
        Partition a linked list around value x:
        All nodes with value < x come before nodes with value >= x.
        Relative order within each group is preserved.
        """
        # Step 1: Create two dummy nodes to build separate lists
        # slist: dummy head for the "small" list (values < x)
        # blist: dummy head for the "big" list (values >= x)
        slist, blist = ListNode(), ListNode()
        
        # Step 2: Working pointers for appending nodes
        small = slist   # Points to the last node in the small list
        big = blist     # Points to the last node in the big list
        
        # Step 3: Traverse the original list
        while head:
            if head.val < x:
                # Step 3.1: Node belongs to small partition
                small.next = head   # Append to small list
                small = small.next  # Move working pointer forward
            else:
                # Step 3.2: Node belongs to big partition
                big.next = head     # Append to big list
                big = big.next      # Move working pointer forward
            
            # Move to next node in original list
            head = head.next
        
        # Step 4: Connect the two partitions
        # End of small list points to start of big list
        small.next = blist.next
        
        # Step 5: Terminate the big list (important to avoid cycles if original had them)
        big.next = None
        
        # Step 6: Return the head of the partitioned list (skip the dummy)
        return slist.next