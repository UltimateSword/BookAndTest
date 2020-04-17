def solution(nums: list) -> list:
    if len(nums) == 1:
        return [0, 0]

    sum_index = []
    corr_sum = 0
    for k, v in enumerate(nums):
        corr_sum += v
        sum_index.append((k, corr_sum))
    print(sum_index)
    sum_index = sorted(sum_index, key=lambda x: x[1])
    print(sum_index)
    min_close = float('inf')
    result = []
    for i in range(1, len(sum_index)):
        one_close = abs(sum_index[i][1] - sum_index[i - 1][1])
        if one_close < min_close:
            min_close = one_close
            result = []
            result.append(min(sum_index[i][0], sum_index[i - 1][0])+1)
            result.append(max(sum_index[i][0], sum_index[i - 1][0]))
            print(min_close, result)
        if abs(sum_index[i][1]) < min_close:
            result = [0, i]
            print(result)
            min_close = abs(sum_index[i][1])
        if abs(sum_index[i-1][1]) < min_close:
            result = [0, i-1]
            print(result)
            min_close = abs(sum_index[i-1][1])
    return result

if __name__ == "__main__":
    # [-3,1,1,-3,5]
    # [6, -4, -8, 3, 1, 7]
    print(solution([3, -3, 5]))

