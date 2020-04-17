def solution(nums, target):
    if len(nums) == 0:
        return -1
    start, end = 0, len(nums) - 1
    res = -1
    while start <= end:
        mid = start + (end - start) // 2
        if nums[mid] > target:
            end = mid - 1
        elif nums[mid] == target:
            res = mid
            end = mid - 1
        else:
            start = mid + 1
    if res >= 0:
        return res
    else:
        return -1


if __name__ == '__main__':
    print(solution([3, 4, 5, 8, 8, 8, 8, 10, 13, 14], 8))
