class ListNode():

    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList():

    def __init__(self, first, *k):
        self.head = ListNode(first)
        temp = self.head
        for i in k:
            temp.next = ListNode(i)
            temp = temp.next

    def reverse(self):
        prev = None
        while self.head:
            temp = self.head.next
            self.head.next = prev
            prev = self.head
            self.head = temp
        self.head = prev
        return repr(self)

    def __repr__(self):
        s = '{}'.format(self.head.val)
        temp = self.head.next
        while temp:
            s += ','
            s += str(temp.val)
            temp = temp.next
        return "LinkedList({})".format(s)

"""
由于单向链表每个节点只有一个后继指针，因此有些操作十分复杂：
例如反向遍历链表，获得链表中一个元素前面的元素。这些操作单链表都需要多次遍历，十分的浪费资源。
因此我们引入了双向链表这一概念。
双向链表较之单向链表最大的区别就是一个节点不仅仅拥有后继指针指向它的后一个节点，
而且还拥有一个前驱指针指向它前一个节点。因此，对于双向链表来说。
反向遍历链表和访问链表中某个元素前一个元素都可以通过它的前驱指针较为简单的完成。

"""
class DoubleLinked():

    def __init__(self, val):
        self.val = val
        self.pre = self.next = None


class DoubleList():

    def __init__(self, first, *k):
        self.head = DoubleLinked(first)
        temp = self.head
        for i in k:
            item = DoubleLinked(i)
            item.pre = temp
            temp.next = item
            temp = temp.next
        self.tail = temp

    def reverse(self):
        pre = None
        while self.head:
            # 1.遍历每一个节点 2.pre和next互唤。
            temp = self.head
            self.head = self.head.next
            temp.next = temp.pre
            temp.pre = self.head
        self.head = temp

    def __repr__(self):
        s = 'head:{}'.format(self.head.val)
        temp = self.head.next
        while temp:
            s += ','
            s += str(temp.val)
            temp = temp.next
        return s