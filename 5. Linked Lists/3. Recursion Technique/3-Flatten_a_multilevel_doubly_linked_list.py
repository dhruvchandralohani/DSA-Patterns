"""
Flatten a Multilevel Doubly Linked List

You are given a doubly linked list, which contains nodes that have a next pointer, a previous pointer, and an additional child pointer. This child pointer may or may not point to a separate doubly linked list, also containing these special nodes. These child lists may have one or more children of their own, and so on, to produce a multilevel data structure as shown in the example below.

Given the head of the first level of the list, flatten the list so that all the nodes appear in a single-level, doubly linked list. Let curr be a node with a child list. The nodes in the child list should appear after curr and before curr.next in the flattened list.

Return the head of the flattened list. The nodes in the list must have all of their child pointers set to null.

Example 1:

Input: head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
Output: [1,2,3,7,8,11,12,9,10,4,5,6]
Explanation: The multilevel linked list in the input is shown.
After flattening the multilevel linked list it becomes:

Example 2:

Input: head = [1,2,null,3]
Output: [1,3,2]
Explanation: The multilevel linked list in the input is shown.
After flattening the multilevel linked list it becomes:

Example 3:

Input: head = []
Output: []
Explanation: There could be empty list in the input.

Constraints:

The number of Nodes will not exceed 1000.
1 <= Node.val <= 105

How the multilevel linked list is represented in test cases:

We use the multilevel linked list from Example 1 above:

 1---2---3---4---5---6--NULL
         |
         7---8---9---10--NULL
             |
             11--12--NULL
The serialization of each level is as follows:

[1,2,3,4,5,6,null]
[7,8,9,10,null]
[11,12,null]
To serialize all levels together, we will add nulls in each level to signify no node connects to the upper node of the previous level. The serialization becomes:

[1,    2,    3, 4, 5, 6, null]
             |
[null, null, 7,    8, 9, 10, null]
                   |
[            null, 11, 12, null]
Merging the serialization of each level and removing trailing nulls we obtain:

[1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
"""
from typing import Optional
# Definition for a Node.
class Node:
    def __init__(self, val, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        Flatten a multilevel doubly linked list into a single-level doubly linked list.
        
        The list can have child pointers that point to separate sub-lists.
        We need to connect all nodes in pre-order traversal order while maintaining prev/next links.
        
        Approach: Iterative with a stack to handle backtracking when we finish a child list.
        """
        # Step 1: Handle empty list
        if not head:
            return None
        
        # Step 2: Initialize stack and current pointer
        stack = []                    # Stack to store nodes we need to visit later (next siblings)
        current = head                # Current node we're processing
        
        # Step 3: Traverse using current pointer and stack for backtracking
        while current or stack:
            # Step 3.1: If current node has a child, process the child list first
            if current.child:
                # If there's a next node, save it on stack (we'll come back to it after child)
                if current.next:
                    stack.append(current.next)
                
                # Connect current node to its child (flatten)
                current.next = current.child
                current.child.prev = current   # Maintain doubly linked property
                
                # Remove the child pointer (no longer needed)
                current.child = None
            
            # Step 3.2: If no next node but stack has saved nodes → continue from saved next
            elif not current.next and stack:
                next_node = stack.pop()        # Retrieve the saved next sibling
                current.next = next_node       # Connect current to saved node
                next_node.prev = current       # Maintain doubly linked property
            
            # Step 3.3: Move to the next node in the flattened list
            current = current.next
        
        # Step 4: Return the original head (now the head of the flattened list)
        return head