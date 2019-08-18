# !/usr/bin/env python3
# coding: utf-8
# Author: initiald0824
# Date: 2019/8/18 2:03

# 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
#
# 例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.
#
# 与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
#
#
import sys


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 3:
            return sum(nums)
        nums.sort()
        dis = sys.maxsize
        res = None
        for index, num in enumerate(nums):
            if index > 1 and nums[index] == nums[index-1]:
                continue
            i = index + 1
            j = len(nums) - 1
            while i < j:
                sum_val = num + nums[i] + nums[j]
                if sum_val > target:
                    j -= 1
                    while nums[j] == nums[j+1] and i < j:
                        j -= 1
                elif sum_val < target:
                    i += 1
                    while nums[i] == nums[i-1] and i < j:
                        i += 1
                else:
                    return target
                new_dis = abs(target-sum_val)
                if new_dis < dis:
                    dis = new_dis
                    res = sum_val
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.threeSumClosest([-1, 2, 1, -4], 1))

