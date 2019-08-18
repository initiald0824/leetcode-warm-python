#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author initiald0824
# @Time 2019/8/18 0:02

# 给定一个未排序的整数数组，找出最长连续序列的长度。
#
# 要求算法的时间复杂度为 O(n)。
#
# 示例:
#
# 输入: [100, 4, 200, 1, 3, 2]
# 输出: 4
# 解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。
#


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        record = set(nums)
        max_len = 0
        for num in nums:
            cnt = 1
            index = 1
            while num-index in record:
                record.remove(num-index)
                index += 1
                cnt += 1
            index = 1
            while num+index in record:
                record.remove(num+index)
                index += 1
                cnt += 1
            if max_len < cnt:
                max_len = cnt
        return max_len


if __name__ == '__main__':
    solution = Solution()
    print(solution.longestConsecutive([100, 4, 200, 1, 3, 2]))



