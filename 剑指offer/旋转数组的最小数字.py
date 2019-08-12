# !/usr/bin/env python3
# coding: utf-8
# Author: initiald0824
# Date: 2019/8/12 23:13

# 把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
# 输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。
# 例如数组{3, 4, 5, 1, 2}为{1, 2, 3, 4, 5}的一个旋转，该数组的最小值为1。


# 二分查找
def binary_search(nums, target):
    lo = 0
    hi = len(nums) - 1
    while lo <= hi:
        mid = int((lo + hi) / 2)
        if nums[mid] == target:
            return True
        elif nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return False


def get_rotate_min(nums):
    if not nums:
        return None
    lo = 0
    hi = len(nums) - 1
    mid = lo
    while nums[lo] >= nums[hi]:
        mid = int((lo + hi) / 2)
        if lo == hi - 1:
            mid = hi
            break
        if nums[mid] == nums[lo] and nums[lo] == nums[hi]:
            return min(nums)
        elif nums[mid] >= nums[lo]:
            lo = mid
        elif nums[mid] <= nums[hi]:
            hi = mid
    return nums[mid]


if __name__ == '__main__':
    array = [3, 4, 5, 1, 2]
    print(get_rotate_min(array))
