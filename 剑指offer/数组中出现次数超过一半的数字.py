# !/usr/bin/env python3
# coding: utf-8
# Author: initiald0824
# Date: 2019/8/15 23:53

# 数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
# 由于数组2在数组里出现了5次，超过数组长度的一半，因此输出2。


def get_count_max(nums):
    if not nums:
        return 0
    cnt = 1
    res = nums[0]
    for num in nums[1:]:
        if cnt == 0:
            cnt = 1
            res = num
        elif num == res:
            cnt += 1
        else:
            cnt -= 1
    return res


if __name__ == '__main__':
    print(get_count_max([1, 2, 3, 2, 2, 2, 5, 4, 2]))
