class Solution_low:
    def threeSum(self, nums: list) -> list:
        res = []
        hash = set()
        for i in range(0, len(nums)):
            two_sum = 0 - nums[i]
            dp = set()
            for j in range(i + 1, len(nums)):
                if two_sum - nums[j] in dp:
                    one = sorted([nums[i], nums[j], two_sum - nums[j]])
                    one_hash = ''.join([str(_) for _ in one])
                    if one_hash not in hash:
                        res.append(one)
                        hash.add(one_hash)
                else:
                    dp.add(nums[j])
        return res


class Solution:

    def threeSum(self, nums: list) -> list:
        nums = sorted(nums)
        if len(nums) < 3:
            return []
        res, i = [], 0
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:  # 两个指针分别从前向后 从后向前找
                tmp = nums[left] + nums[right]  # 后两位值
                if tmp + nums[i] == 0:  # 判断nums[i]==0
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                elif tmp + nums[i] < 0:  # 后两位值和当前值相比太小 增加left
                    left += 1
                else:  # 太大减少right
                    right -= 1
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.threeSum([-1, 0, 1, 2, -1, -4]))
