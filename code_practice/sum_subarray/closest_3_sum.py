"""
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum-closest
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def threeSumClosest(self, nums: list, target: int) -> int:
        nums = sorted(nums)
        one = sum(nums[0:3])
        for i in range(len(nums)):
            l, r, new_target = i+1, len(nums) - 1, target - nums[i]
            while l < r:
                # print(nums[l] + nums[r], l, r, one, new_target)
                if abs(target - nums[i] - nums[l] - nums[r]) < abs(target - one):
                    one = nums[i] + nums[l] + nums[r]
                if nums[l] + nums[r] < new_target:
                    l += 1
                elif nums[l] + nums[r] > new_target:
                    r -= 1
                else:
                    return target
        return one


if __name__ == '__main__':
    S = Solution()
    # [-4, -1, 1 2]
    print(S.threeSumClosest([-1, 2, 1, -4], 1))

