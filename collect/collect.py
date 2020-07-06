# 快速排序
def partial(nums, target):
    lft = [i for i in nums if i < target]
    rgt = [i for i in nums if i > target]
    mid = [i for i in nums if i==target]
    return lft, mid, rgt


def quick_sort(nums:list) ->list:
    n = len(nums)
    if n == 0:
        return []
    elif n == 1:
        return nums
    target = nums[0]
    lft, mid, rgt = partial(nums, target)
    return quick_sort(lft) + mid + quick_sort(rgt)


# 归并排序
def merge(left, right):
    ans = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            ans.append(left[i])
            i += 1
        else:
            ans.append(right[j])
            j += 1

    if i == len(left):
        ans.extend(right[j:])
    else:
        ans.extend(left[i:])
    return ans


def merge_sort(lists):
    if len(lists) <= 1:
        return lists
    middle = len(lists)//2
    left = merge_sort(lists[:middle])
    right = merge_sort(lists[middle:])
    return merge(left, right)


# 堆排序
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # 交换
        heapify(arr, n, largest)


def heapSort(arr):
    n = len(arr)

    # Build a maxheap.
    for i in range(n, -1, -1):
        heapify(arr, n, i)

        # 一个个交换元素
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # 交换
        heapify(arr, i, 0)


if __name__ == '__main__':
    # print(quick_sort([1,2,5,3,7,2,6,1,9]))
    # print(merge_sort([1,2,5,3,7,2,6,1,9]))
    a = [1, 2, 3, 4]
    heapify(a, 2, 1)
    print(a)
