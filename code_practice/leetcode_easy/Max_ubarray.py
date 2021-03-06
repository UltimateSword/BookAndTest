"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.


链接：https://leetcode-cn.com/problems/maximum-subarray

"""

class Solution:
    def maxSubArray(self, nums: list) -> int:
        if len(nums) == 1:
            return nums[0]
        ans = nums[0]
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] = nums[i] + nums[i-1]
            else:
                nums[i] = nums[i]
            ans = max(ans, nums[i])
        return ans