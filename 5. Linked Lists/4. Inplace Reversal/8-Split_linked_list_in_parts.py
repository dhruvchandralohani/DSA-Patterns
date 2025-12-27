"""
Split Linked List in Parts

Given the head of a singly linked list and an integer k, split the linked list into k consecutive linked list parts.

The length of each part should be as equal as possible: no two parts should have a size differing by more than one. This may lead to some parts being null.

The parts should be in the order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal to parts occurring later.

Return an array of the k parts.

Example 1:

Input: head = [1,2,3], k = 5
Output: [[1],[2],[3],[],[]]
Explanation:
The first element output[0] has output[0].val = 1, output[0].next = null.
The last element output[4] is null, but its string representation as a ListNode is [].

Example 2:

Input: head = [1,2,3,4,5,6,7,8,9,10], k = 3
Output: [[1,2,3,4],[5,6,7],[8,9,10]]
Explanation:
The input has been split into consecutive parts with size difference at most 1, and earlier parts are a larger size than the later parts.
 
Constraints:

The number of nodes in the list is in the range [0, 1000].
0 <= Node.val <= 1000
1 <= k <= 50
"""
from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        """
        Split a linked list into k consecutive parts.
        Each part should be as equal in length as possible.
        The earlier parts should be larger (or equal) if the total length is not divisible by k.
        Return a list of k linked list heads (some may be None if k > total length).
        """
        # Step 1: Calculate the total length of the linked list
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        
        # Step 2: Determine the base size of each part and how many parts get an extra node
        # part_size: minimum size for each of the k parts
        # larger_parts: number of parts that get one extra node (remainder)
        part_size = length // k          # integer division → base size
        larger_parts = length % k        # remainder → first 'larger_parts' parts get +1
        
        # Step 3: Initialize the result list to hold k sublist heads
        result = []
        
        # Step 4: Traverse the original list and split into k parts
        current = head
        for i in range(k):
            # Calculate the size of the current part
            # First 'larger_parts' parts get (part_size + 1), others get part_size
            sublist_size = part_size + 1 if i < larger_parts else part_size
            
            # If sublist_size is 0 → this part is empty (happens when k > length)
            if sublist_size == 0:
                result.append(None)
            else:
                # Start of current sublist
                sublist_head = current
                
                # Move current forward (sublist_size - 1) times to reach the end of this part
                for _ in range(sublist_size - 1):
                    current = current.next
                
                # Save the start of the next part
                next_node = current.next
                
                # Break the link to separate this sublist
                current.next = None
                
                # Add the sublist head to result
                result.append(sublist_head)
                
                # Move to the start of the next part
                current = next_node
        
        # Step 5: Return the list of k sublist heads
        return result