"""
Palindrome Linked List

Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

Example 1:

Input: head = [1,2,2,1]
Output: true

Example 2:

Input: head = [1,2]
Output: false

Constraints:

The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9

Follow up: Could you do it in O(n) time and O(1) space?
"""
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverse(self, head: ListNode) -> ListNode:
        """
        Helper function: Reverse a singly-linked list iteratively.
        Returns the new head of the reversed list.
        """
        prev = None          # Step 1: Points to the reversed portion (starts as None)
        cur = head           # Step 2: Current node being processed
        
        # Step 3: Reverse links one by one
        while cur:
            temp = cur.next          # Save next node before overwriting the link
            cur.next = prev          # Reverse the arrow
            prev = cur               # Move prev forward (include current node)
            cur = temp               # Move cur forward to next unreversed node
        
        # Step 4: prev now points to the last node processed → new head
        return prev

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """
        Check if a singly-linked list is a palindrome.
        
        Approach:
        1. Use slow/fast pointers to find the middle of the list.
        2. Reverse the second half of the list.
        3. Compare the first half with the reversed second half.
        """
        # Edge case: empty or single node → always palindrome
        if not head or not head.next:
            return True
        
        # ───────────────────────────────
        # Step 1: Find the middle using Tortoise & Hare
        # ───────────────────────────────
        slow = fast = head
        while fast and fast.next:
            slow = slow.next        # moves 1 step
            fast = fast.next.next   # moves 2 steps
        # After loop: slow points to the start of the second half
        
        # ───────────────────────────────
        # Step 2: Reverse the second half
        # ───────────────────────────────
        rev = self.reverse(slow)
        
        # ───────────────────────────────
        # Step 3: Compare first half with reversed second half
        # ───────────────────────────────
        while rev:                     # Traverse until end of reversed part
            if head.val != rev.val:    # Values don't match → not palindrome
                return False
            head = head.next           # Move in first half
            rev = rev.next             # Move in reversed second half
        
        # Step 4: All compared nodes matched → palindrome
        return True