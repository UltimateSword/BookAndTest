from collections import Counter, deque
import heapq


class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = self.right = None


class Travel(object):
    def __init__(self):
        self.res = []

    def pre_order(self, root):
        if root:
            self.res.append(root.val)
            self.pre_order(root.left)
            self.pre_order(root.right)

    def mid_order(self, root):
        if root:
            self.mid_order(root.left)
            self.res.append(root.val)
            self.mid_order(root.right)

    def post_order(self, root):
        if root:
            self.post_order(root.right)
            self.post_order(root.left)
            self.res.append(root.val)

# binary search tree: bst,二叉查找树,中序遍历得到有序数组的树,即右节点值大约左节点的树
# 优点是将有序数组查找的方便性和链表插入的方便性结合了起来


class HuffNode(object):

    def __init__(self, val, char=''):
        self.val = val
        self.char = char
        self.coding = ''
        self.left = self.right = None

    def __eq__(self, other):
        return self.val == other.val

    def __lt__(self, other):
        return self.val < other.val

    def __gt__(self, other):
        return self.val > other.val


class HuffmanCompression(object):
    def __init__(self, string):
        self.string = string
        counter = Counter(string)
        heap = []
        for char, cnt in counter.items():
            heapq.heappush(heap, HuffNode(cnt, char))

        while len(heap) != 1:
            left = heapq.heappop(heap)
            right = heapq.heappop(heap)
            new_node = HuffNode(left.val+right.val)
            new_node.left, new_node.right = left, right
            heapq.heappush(heap, new_node)

        self.root = heap[0]
        self.s2b = {}
        self.bfs_encode(self.root, self.s2b)

    @staticmethod
    def bfs_encode(root, s2b):
        queue = deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if node.char:
                s2b[node.char] = node.coding
                continue
            if node.left:
                node.left.coding = node.coding + '0'
                queue.append(node.left)
            if node.right:
                node.right.coding = node.coding + '1'
                queue.append(node.right)

    def compress(self):
        bits = ''
        for char in self.string:
            bits += self.s2b[char]
        return bits

    def uncompress(self, bits):
        string = ''
        root = self.root
        for i in bits:
            if i == '0':
                root = root.left
            else:
                root = root.right
            if root.char:
                string += root.char
                root = self.root
        return string


if __name__ == '__main__':
    s = HuffmanCompression('123aaaaa' + 'a'*1000)
    cop = s.compress()
    print(cop)
    print(s.uncompress(cop))
