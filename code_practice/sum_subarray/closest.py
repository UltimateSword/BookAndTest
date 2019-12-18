def solution(nums: list) -> list:
    sum_index = []
    corr_sum = 0
    for k, v in enumerate(nums):
        corr_sum += v
        sum_index.append((k, corr_sum))
    sum_index = sorted(sum_index, key=lambda x: x[1])

    min_close = abs(sum_index[0][1] - sum_index[-1][1])
    result = []
    for i in range(1, len(sum_index)):
        one_close = abs(sum_index[i][1] - sum_index[i - 1][1])
        if one_close < min_close:
            min_close = one_close
            result = [sum_index[i][0], sum_index[i - 1][0]]
    return sorted(result)

if __name__ == "__main__":
    print(solution([-3,1,1,3,-5]))

