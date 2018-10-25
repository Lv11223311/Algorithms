""" 
Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5 
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElement(self, head, val):

        dummy = ListNode(-1)
        dummy.next = head
        pointer = dummy

        while pointer.next:

            if pointer.next.val == val:
                pointer.next = pointer.next.next
            else:
                pointer = pointer.next

        return dummy.next