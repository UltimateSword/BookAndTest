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
        for i in range(len(nums)):
            if nums[i] < 0:
                

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


if __name__ == '__main__':
    s = Solution()
    print(s.threeSum([-1, 0, 1, 2, -1, -4]))
