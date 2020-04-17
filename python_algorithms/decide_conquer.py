# 分治法:比较典型的例子就是二分查找lg(n)和快速排序nlg(n)(最差时达到n2,归并排序一直是nlog(n)


class QuickSort(object):  # 快排
    @staticmethod
    def partial(queue):
        one = queue[0]
        rest = queue[1:]
        return [i for i in rest if i <= one], one, [i for i in rest if i > one]

    def quick_sort(self, queue):
        if len(queue) <= 1:
            return queue
        left, num, right = self.partial(queue)
        return self.quick_sort(left) + [num] + self.quick_sort(right)


def mergesort(seq):
    mid = len(seq) // 2
    lft, rgt = seq[:mid], seq[mid:]
    if len(lft) > 1:
        lft = mergesort(lft)
    if len(rgt) > 1:
        rgt = mergesort(rgt)
    res = []
    while lft and rgt:
        if lft[-1] >= rgt[-1]:
            res.append(lft.pop())
        else:
            res.append(rgt.pop())
    res.reverse()
    return (lft or rgt) + res


def binary_search(nums, target):
    le, ri = 0, len(nums)-1
    while le <= ri:
        mid = (ri + le) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            le = mid + 1
        else:
            ri = mid - 1
    return le


# 二分搜索树
class Node(object):
    left = None
    right = None

    def __init__(self, key, val):
        self.key = key
        self.val = val


def insert(node, key, val):
    if node is None:
        return Node(key, val)
    if node.key == key:
        node.val = val
    elif node.key > key:
        node.left = insert(node.left, key, val)
    else:
        node.right = insert(node.right, key, val)


def search(node, key):
    if node is None:
        raise KeyError
    if node.key == key:
        return node.val
    elif node.key < key:
        return search(node.right, key)
    else:
        return search(node.left, key)


class Tree(object):
    root = None

    def __setitem__(self, key, value):
        self.root = insert(self.root, key, value)

    def __getitem__(self, item):
        return search(self.root, item)

    def __contains__(self, item):
        try:
            search(self.root, item)
        except KeyError:
            return False
        return True


if __name__ == '__main__':
    print('1. 快排,归并排序测试')
    Qs = QuickSort()
    assert Qs.quick_sort([5, 6, 6, 6, 3, 4, 1, 9, 8, 7]) == mergesort([5, 6, 6, 6, 3, 4, 1, 9, 8, 7])
    print('2. 二分查找测试:二分查找注意点: n = len(nums) - 1, while l < r,return l')
    print(binary_search([1, 2, 3, 4, 4, 4, 5, 7, 9], 6))
    print('3. 二叉搜索树: 测试')
    bt = Tree()
    bt['a'] = 42
    print(bt['a'], 'a' in bt)
