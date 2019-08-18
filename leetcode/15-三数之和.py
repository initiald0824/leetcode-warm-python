# !/usr/bin/env python3
# coding: utf-8
# Author: initiald0824
# Date: 2019/8/18 1:30

# 给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。
#
# 注意：答案中不可以包含重复的三元组。
#
# 例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
#
# 满足要求的三元组集合为：
# [
#  [-1, 0, 1],
#  [-1, -1, 2]
# ]
#
#


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        if len(nums) < 3:
            return res
        nums.sort()
        for index, num in enumerate(nums):
            if index > 0 and nums[index] == nums[index-1]:
                continue
            i = index + 1
            j = len(nums) - 1
            while i < j:
                sum_val = num + nums[i] + nums[j]
                if sum_val == 0:
                    res.append([num, nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while nums[i] == nums[i-1] and i < j:
                        i += 1
                    while nums[j] == nums[j+1] and i < j:
                        j -= 1
                elif sum_val < 0:
                    i += 1
                    while nums[i] == nums[i-1] and i < j:
                        i += 1
                else:
                    j -= 1
                    while nums[j] == nums[j+1] and i < j:
                        j -= 1
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.threeSum([-2, 0, 1, 1, 2]))

