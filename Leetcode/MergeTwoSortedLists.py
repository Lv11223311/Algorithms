""" Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4 """

class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None
        

def mergeTwoLists(l1, l2):
    # recursively
    if not l1 or not l2:
        return l1 or l2

    if l1.val< l2.val:
        l1.next = mergeTwoLists(l1.next, l2)
        return l1
    else:
        l2.next = mergeTwoLists(l1, l2.next)
        return l2

def mergeTwoLists2(l1, l2):
    # iteratively
    head = cur = ListNode(0)
    # linked-list，设置一个head，不断往下排
    while l1 and l2:
        if l1.val < l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next
    cur.next = l1 or l2
    return head.next


