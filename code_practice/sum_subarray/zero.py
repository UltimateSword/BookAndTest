def solution(nums: list) -> list:
    hash = dict()
    corr_sum = 0
    for i in range(len(nums)):
        corr_sum += nums[i]
        if corr_sum == 0:
            return [0, i]
        elif corr_sum in hash:
            return [hash[corr_sum] + 1, i]
        else:
            hash[corr_sum] = i


if __name__ == "__main__":
    # 1,2,-1,1
    print(solution([1,1,-3,2]))