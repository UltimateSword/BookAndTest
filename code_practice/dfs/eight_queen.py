class Solution:
    def solveNQueens(self, n: int):
        board = [['.']*n for _ in range(n)]

        def is_valid(board, r, c):
            for i in range(n):
                for j in range(n):
                    if board[i][j] == 'Q' and (i == r or j == c or abs(i-r) == abs(j-c)):
                        return False
            return True

        res = []

        def recall(board, row):
            if row == n:
                res.append([''.join(i) for i in board])
                return
            for c in range(n):
                print(is_valid(board, row, c))
                if not is_valid(board, row, c):
                    continue
                board[row][c] = 'Q'
                recall(board, row + 1)
                board[row][c] = '.'

        recall(board, 0)
        return res


if __name__ == '__main__':
    s = Solution()
    res = s.solveNQueens(4)
    print(len(res), res)
# 23