"""
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        cur = head
        l = 0
        while cur:
            cur = cur.next
            l += 1
        dummy = ListNode(0)  # 哑结点，防止只有一项也需要移除时候的判断
        dummy.next = head
        new = dummy
        l = l - n  # 注意5项-2项=3项 循环三次 1,2,3 不包括0
        while l > 0:
            l -= 1
            new = new.next
        new.next = new.next.next
        return dummy.next