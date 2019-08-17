# !/usr/bin/env python3
# coding: utf-8
# Author: initiald0824
# Date: 2019/8/17 14:21

# 一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。
# 要求时间复杂度是O(n),空间复杂度是O(1)


def get_only_once(nums):
    if not nums:
        return None
    xor_val = get_xor_val(nums)
    index = get_1st_bit(xor_val)
    left_nums = []
    right_nums = []
    for num in nums:
        if is_bit_1(num, index):
            left_nums.append(num)
        else:
            right_nums.append(num)
    left, right = get_xor_val(left_nums), get_xor_val(right_nums)
    return left, right


def get_xor_val(nums):
    if not nums:
        return None
    xor_val = nums[0]
    for num in nums[1:]:
        xor_val ^= num
    return xor_val


def is_bit_1(num, index):
    if num & (1 << index) != 0:
        return True
    else:
        return False


def get_1st_bit(num):
    cnt = 32
    index = 0
    while cnt:
        cnt -= 1
        if num & 1 != 0:
            return index
        else:
            index += 1
            num = num >> 1


if __name__ == '__main__':
    array = [2, 4, 3, 6, 3, 2, 5, 5]
    print(get_only_once(array))
