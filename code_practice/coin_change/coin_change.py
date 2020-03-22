"""
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/coin-change
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

"""
某些情况下可以用贪心算法,其他情况要用动态规划.但是我不知道什么时候可以用贪心算法.贪心算法的效率是最高的.
"""


# dp
class Solution:
    def coinChange_dp_recursion(self, coins: list, amount: int) -> int:
        map_dict = dict()

        def dp(n: int) -> int:
            if n == 0:
                return 0
            if n < 0:
                return -1
            res = amount + 1
            if n in map_dict:
                return map_dict[n]
            for coin in coins:
                sub_res = dp(n-coin)
                if sub_res == -1:
                    continue
                res = min(res, 1+sub_res)
            map_dict[n] = res if res != amount + 1 else -1
            return map_dict[n]
        return dp(amount)

    def solution_for_recursion(self, coins: list, amount: int) -> int:
        dp = [amount+1] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount+1):
            for c in coins:
                if i - c < 0:
                    continue
                dp[i] = min(dp[i], dp[i-c]+1)
        if dp[amount] == amount + 1:
            return -1
        else:
            return dp[amount]

    def solution_dfs(self, coins: list, amount: int) -> int:
        if amount == 0:
            return 0

        def dfs(amount, res):
            pass




if __name__ == '__main__':
    s = Solution()
    print(s.coinChange_dp_recursion([1, 2, 5], 11))