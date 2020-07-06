class Solution:
    def waysToChange(self, n: int) -> int:
        coins = [1, 5, 10, 25]
        dp = [0] * (n + 1)
        dp[0] = 1
        for coin in coins :
            for i in range(coin, n + 1) :
                dp[i] = (dp[i] + dp[i - coin])
                
        print(dp)
        return dp[n] % 1000000007


if __name__ == '__main__':
    s = Solution()
    s.waysToChange(6)