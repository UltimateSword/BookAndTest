class Solution:
    def removeDuplicates(self, nums: list) -> int:
        i = 0
        while i < len(nums) - 1:
            if nums[i + 1] == nums[i]:
                del nums[i + 1]
            i += 1
        return len(nums)


if __name__ == '__main__':
    s = Solution()
    print(s.removeDuplicates([1, 1, 2, 2]))
