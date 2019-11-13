class ListNode():

    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList():

    def __init__(self, first, *k):
        self.link = ListNode(first)
        temp = self.link
        for i in k:
            temp.next = ListNode(i)
            temp = temp.next

    def reverse(self):
        prev = None
        while self.link:
            temp = self.link.next
            self.link.next = prev
            prev = self.link
            self.link = temp
        self.link = prev
        return repr(self)

    def __repr__(self):
        s = '{}'.format(self.link.val)
        temp = self.link.next
        while temp:
            s += ','
            s += str(temp.val)
            temp = temp.next
        return "LinkedList({})".format(s)

