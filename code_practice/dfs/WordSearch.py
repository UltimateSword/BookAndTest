class Solution:
    def exist(self, board: list, word: str) -> bool:
        if not board:
            return word == ''
        m, n = len(board), len(board[0])
        directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        marked = [[False] * n for _ in range(m)]  # 防止重复的记录表，类似动态规划思想

        def search_word(cur, x, y):  # 主要逻辑
            if cur == len(word) - 1:  # 最后一位不需要递归下去
                return board[x][y] == word[cur]
            if board[x][y] == word[cur]:  # 不相等不需要递归直接返回false
                marked[x][y] = True  # 处理逻辑开始 首先是边界 然后是递归比较
                for direction in directions:
                    new_x, new_y = x + direction[0], y+direction[1]
                    if 0 <= new_x < m and 0 <= new_y < n and not marked[new_x][new_y] and search_word(cur+1, new_x, new_y):
                        return True
                marked[x][y] = False  # 恢复之前状态
            return False
        for i in range(m):
            for j in range(n):
                if search_word(0, i, j):
                    return True
        return False


if __name__ == '__main__':
    s = Solution()
    s.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
            "ABCCED")
    print()
