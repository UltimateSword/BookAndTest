"""
On an 8 x 8 chessboard, there is one white rook.  There also may be empty squares, white bishops, and black pawns.  These are given as characters 'R', '.', 'B', and 'p' respectively. Uppercase characters represent white pieces, and lowercase characters represent black pieces.

The rook moves as in the rules of Chess: it chooses one of four cardinal directions (north, east, west, and south), then moves in that direction until it chooses to stop, reaches the edge of the board, or captures an opposite colored pawn by moving to the same square it occupies.  Also, rooks cannot move into the same square as other friendly bishops.

Return the number of pawns the rook can capture in one move.

 

Example 1:



Input: [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
Output: 3
Explanation:
In this example the rook is able to capture all the pawns.
Example 2:



Input: [[".",".",".",".",".",".",".","."],[".","p","p","p","p","p",".","."],[".","p","p","B","p","p",".","."],[".","p","B","R","B","p",".","."],[".","p","p","B","p","p",".","."],[".","p","p","p","p","p",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
Output: 0
Explanation:
Bishops are blocking the rook to capture any pawn.
Example 3:



Input: [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","p",".",".",".","."],["p","p",".","R",".","p","B","."],[".",".",".",".",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."]]
Output: 3
Explanation:
The rook can capture the pawns at positions b5, d6 and f5.
 

Note:

board.length == board[i].length == 8
board[i][j] is either 'R', '.', 'B', or 'p'
There is exactly one cell with board[i][j] == 'R'


链接：https://leetcode-cn.com/problems/available-captures-for-rook

"""


class Solution:
    def numRookCaptures(self, board: list) -> int:
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    ans = 0
                    left, right = i-1 , i+1
                    up, down = j-1, j+1
                    while left >= 0:
                        if board[left][j] == '.':
                            left -= 1
                            print(left)
                        elif board[left][j] == 'B':
                            break
                        elif board[left][j] == 'p':
                            ans += 1
                            break
                    while right <= 8:
                        if board[right][j] == '.':
                            right += 1
                        elif board[right][j] == 'B':
                            break
                        elif board[right][j] == 'p':
                            ans += 1
                            break
                    while up >= 0:
                        if board[i][up] == '.':
                            up -= 1
                        elif board[i][up] == 'B':
                            break
                        elif board[i][up] == 'p':
                            ans += 1
                            break
                    while down <= 8:
                        if board[i][down] == '.':
                            down += 1
                        elif board[i][down] == 'B':
                            break
                        elif board[i][down] == 'p':
                            ans += 1
                            break
                    return ans


if __name__ == '__main__':
    s = Solution()
    print(s.numRookCaptures([[".",".",".",".",".",".",".","."],[".","p","p","p","p","p",".","."],[".","p","p","B","p","p",".","."],[".","p","B","R","B","p",".","."],[".","p","p","B","p","p",".","."],[".","p","p","p","p","p",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]))