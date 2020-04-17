def solution(nums: list, k: int) -> list:
    result = []
    hash = dict()
    corr_sum = 0
    for i in range(len(nums)):
        corr_sum += nums[i]
        if corr_sum == k:
            result.append(0)
            result.append(k)
        elif corr_sum - k in hash:
            result.append(hash[corr_sum - k] + 1)
            result.append(i)
        else:
            hash[corr_sum] = i
    return result


if __name__ == "__main__":
    print(solution([1,1,-2], -1))