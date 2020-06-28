"""
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]


链接：https://leetcode-cn.com/problems/4sum

"""


class Solution:
    def fourSum(self, nums: list, target: int) -> list:
        res = []
        nums = sorted(nums)
        for i in range(len(nums)):  # 第一个数nums[i]
            if sum(nums[i:i+4]) > target:
                continue
            if i > 0 and nums[i] == nums[i-1]:
                continue
            new_target1 = target - nums[i]
            for j in range(i+1, len(nums)):  # 第二个数nums[j]
                if sum(nums[j:j+3]) > new_target1:
                    break
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                new_target2 = new_target1 - nums[j]
                map_record = dict()
                for m in range(j+1, len(nums)):
                    if map_record.get(new_target2 - nums[m], 0) == -1:
                        continue
                    if map_record.get(new_target2 - nums[m], 0) > 0:
                        res.append([nums[i], nums[j], nums[m], new_target2-nums[m]])
                        map_record[new_target2 - nums[m]] = -1
                    else:
                        map_record[nums[m]] = 1
        return res


if __name__ == '__main__':
    S = Solution()
    print(S.fourSum([-1,2,2,-5,0,-1,4],
3))  # -5 -4 -3 -1