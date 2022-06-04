#  -*- coding=utf-8 -*-

# 1. 算法步骤
# 从数列中挑出一个元素，称为 "基准"（pivot）;
#
# 重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。在这个分区退出之后，该基准就处于数列的中间位置。这个称为分区（partition）操作；
#
# 递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序；

def quicksort(array):
    size = len(array)
    # todo 递归的退出条件
    if not array or size<2:
        return array

    pivot_idx = 0
    pivot = array[pivot_idx]
    less_part = [array[i] for i in range(size) if array[i] <= pivot and pivot_idx!=i]
    great_part = [array[i] for i in range(size) if array[i] > pivot and pivot_idx!=i]
    return quicksort(less_part) + [pivot] + quicksort(great_part)

