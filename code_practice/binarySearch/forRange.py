def solution(nums, target):
    if not nums:
        return [0, 0]
    start, end = 0, len(nums) - 1
    rst, rend = 0, 0
    while start <= end:
        mid = start + (end - start) // 2
        if nums[mid] == target:
            tmp = mid
            while nums[mid] == target:
                mid -= 1
            while nums[tmp] == target:
                tmp += 1
            return [mid+1, tmp-1]
        elif nums[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return [-1, -1]

if __name__ == "__main__":
    print(solution([5,7,7,8,8,10], 8))