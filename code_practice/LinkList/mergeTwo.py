class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode(-1)
        pre = res
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                res.next = ListNode(l1.val)
                l1 = l1.next
            else:
                res.next = ListNode(l2.val)
                l2 = l2.next
            res = res.next
        if l1 is not None:
            res.next = l1
        else:
            res.next = l2
        return pre.next
