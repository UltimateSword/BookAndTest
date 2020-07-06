"""
A popular masseuse receives a sequence of back-to-back appointment requests and is debating which ones to accept.
 She needs a break between appointments and therefore she cannot accept any adjacent requests.
 Given a sequence of back-to-back appoint­ ment requests, find the optimal (highest total booked minutes)
 set the masseuse can honor. Return the number of minutes.

Note: This problem is slightly different from the original one in the book.

 

Example 1:

Input:  [1,2,3,1]
Output:  4
Explanation:  Accept request 1 and 3, total minutes = 1 + 3 = 4
Example 2:

Input:  [2,7,9,3,1]
Output:  12
Explanation:  Accept request 1, 3 and 5, total minutes = 2 + 9 + 1 = 12
Example 3:

Input:  [2,1,4,5,3,1,1,3]
Output:  12
Explanation:  Accept request 1, 3, 5 and 8, total minutes = 2 + 4 + 3 + 3 = 12


链接：https://leetcode-cn.com/problems/the-masseuse-lcci

"""


class Solution:
    def massage(self, nums: list) -> int:
        n = len(nums)
        dp = nums
        if not nums:
            return 0
        if n == 1:
            return nums[0]
        if nums[1] >= nums[0]:
            dp[1] = nums[1]
        else:
            dp[1] = nums[0]
        for i in range(2, len(nums)):
            new = nums[i] + dp[i-2]
            if new > dp[i-1]:
                dp[i] = new
            else:
                dp[i] = dp[i-1]
        return dp[-1]


class Solution2:
    def caculate(self, l):
        dp = [i for i in l]
        for i in range(2, len(l)):
            dp[i] = max(dp[i-2] + l[i], dp[i-1])
        return dp[-1]



if __name__ == '__main__':
    s = Solution()
    print(s.massage([2,1]))
    s2 = Solution2()
    print(s2.caculate([2,1,4,5,3,1,1,3]))
