def divide(dividend: int, divisor: int) -> int:
    if dividend == 0:
        return 0
    prefix = (dividend < 0) == (divisor < 0)
    dividend = abs(dividend)
    divisor = abs(divisor)

    def recall(d):
        if d < divisor:
            return 0
        cur = divisor  # 被除数
        count = 1
        while cur + cur <= d:
            cur += cur
            count += count
        return count + recall(d-cur)

    if prefix:
        return recall(dividend)
    else:
        return 0 - recall(dividend)


if __name__ == '__main__':
    print(divide(-2147483648, -1))