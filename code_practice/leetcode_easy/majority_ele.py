"""
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2


链接：https://leetcode-cn.com/problems/majority-element

"""


class Soluton(object):
    def majorityElement(self, nums: list) -> int:
        map_count = {}
        n = len(nums) / 2
        for i in nums:
            map_count[i] = map_count.get(i, 0) + 1
            if map_count[i] > n:
                return i