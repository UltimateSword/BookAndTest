class Solution:

    def convert(self, s: str, num_rows: int) -> str:
        if num_rows == 1:
            return s
        z_nums = num_rows - 1
        num_cols = (len(s) // (num_rows + num_rows - 2)) * z_nums
        if len(s) % (num_rows + num_rows - 2) > num_rows:
            num_cols += len(s) % (num_rows + num_rows - 2) - num_rows + 1
        elif len(s) % (num_rows + num_rows - 2) > 0:
            num_cols += 1
        res = [['' for _ in range(num_cols)] for _ in range(num_rows)]
        i = 0
        for c in range(num_cols):
            for r in range(num_rows):
                if i >= len(s):
                    break
                if c % z_nums == 0:  # 是rows - 1的倍数
                    res[r][c] = s[i]
                    i += 1
                elif r == z_nums - (c % z_nums):
                    res[r][c] = s[i]
                    i += 1
        dp = []
        for r in res:
            for c in r:
                if c:
                    dp.append(c)
        return ''.join(dp)


if __name__ == "__main__":
    s = Solution()
    print(s.convert("ABCD", 2))
    print('ACBD')
