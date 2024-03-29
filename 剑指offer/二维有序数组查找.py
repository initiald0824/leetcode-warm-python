# !/usr/bin/env python3
# coding: utf-8
# Author: initiald0824
# Date: 2019/8/10 18:56

# 在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
# 请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
# 1 2 8  9
# 2 4 9  12
# 4 7 10 13
# 6 8 11 15


def find_target(target, array):
    if not array:
        return False
    m = len(array)
    n = len(array[0])
    if m > 0 and n > 0:
        row = 0
        col = n - 1
        while row < m and col > 0:
            if array[row][col] == target:
                return True
            elif array[row][col] < target:
                row += 1
            else:
                col -= 1
    return False


if __name__ == '__main__':
    sorted_array = [
        [1, 2, 8, 9],
        [2, 4, 9, 12],
        [4, 7, 10, 13],
        [6, 8, 11, 15]
    ]
    print(find_target(16, sorted_array))
