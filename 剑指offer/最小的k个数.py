# !/usr/bin/env python3
# coding: utf-8
# Author: initiald0824
# Date: 2019/8/16 0:30

# 输入n个整数，找出其中最小的k个数。例如输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4


def get_max_k(nums, k):
    res = []
    for num in nums:
        if len(res) < k:
            res.append(num)
        else:
            max_val = max(res)
            if max_val > num:
                res.remove(max_val)
                res.append(num)
    return res


if __name__ == '__main__':
    array = [4, 5, 1, 6, 2, 7, 3, 8]
    print(get_max_k(array, 4))
