# !/usr/bin/env python3
# coding: utf-8
# Author: initiald0824
# Date: 2019/8/18 2:39

# 给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，
# 使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。
#
# 注意:
#
# 答案中不可以包含重复的四元组。
#
# 示例：
#
# 给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。
#
# 满足要求的四元组集合为：
# [
#  [-1,  0, 0, 1],
#  [-2, -1, 1, 2],
#  [-2,  0, 0, 2]
# ]
#
#
from collections import defaultdict


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        size = len(nums)
        if size < 4:
            return res
        nums.sort()
        record = defaultdict(list)
        size = len(nums)
        for i in range(size):
            for j in range(i+1, size):
                record[nums[i]+nums[j]].append([i, j])
        used = set()
        for i in range(size):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, size-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                sum_val = nums[i] + nums[j]
                if (target-sum_val) in record:
                    dis_list = record[target-sum_val]
                    for dis in dis_list:
                        if j < dis[0]:
                            r = [nums[i], nums[j], nums[dis[0]], nums[dis[1]]]
                            if str(r) not in used:
                                res.append(r)
                                used.add(str(r))
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.fourSum([0, 0, 0, 0], 0))


