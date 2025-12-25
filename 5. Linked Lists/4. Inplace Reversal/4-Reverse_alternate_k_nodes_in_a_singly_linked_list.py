# Python program to reverse alternate k nodes
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None


def kAltReverse(head, k):

    # Pointer to the tail of the
    # previous segment
    prev_tail = None
    rev = True
    curr = head

    while curr:

        # Reverse the next k nodes
        if rev == True:

            # Mark the head of the current segment
            seg_head = curr
            prev = None

            # Reverse the current segment of k nodes
            for _ in range(k):
                if curr is None:
                    break
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            # Update the head of the list 
            # if this is the first segment
            if prev_tail is None:
                head = prev
            else:
                # Link previous segment with
                # the current reversed segment
                prev_tail.next = prev

            # Update the tail of the current segment
            prev_tail = seg_head
            rev = False
        else:

            # Skip the next k nodes without reversing
            prev_tail.next = curr
            for _ in range(k):
                if curr is None:
                    break
                prev_tail = curr
                curr = curr.next
            rev = True

    return head


def print_list(node):
    curr = node
    while curr:
        print(curr.data, end=" ")
        curr = curr.next
    print()


if __name__ == "__main__":
  
    # Hardcoded linked list: 1->2->3->4->5->6
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head = kAltReverse(head, 2)
    print_list(head)