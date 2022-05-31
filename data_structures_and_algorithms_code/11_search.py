# -*- coding: utf-8 -*-

number_list = [0, 1, 2, 3, 4, 5, 6, 7]

def linear_search(value, iterable):
    for index, val in enumerate(iterable):
        if val == value:
            return index
    return -1

assert linear_search(5, number_list) == 5


def linear_search_v2(predicate, iterable):
    for index, val in enumerate(iterable):
        if predicate(val):
            return index
    return -1

assert linear_search_v2(lambda x: x==5, number_list) == 5


# 递归方式实现查找
def linear_search_recusive(array, value):
    if len(array) == 0:
        return -1
    index = len(array) -1
    if array[index] == value:
        return index
    return linear_search_recusive(array[0:index], value)


# 二分查找实现搜索
def binary_search_recursive(sorted_array, beg, end, val):
    if beg >= end:
        return -1
    mid = int((beg + end)/2)
    if sorted_array[mid] == val:
        return mid
    elif sorted_array[mid] > val:
        return binary_search_recursive(sorted_array, beg, mid, val)
    else:
        return binary_search_recursive(sorted_array, mid+1, end, val)
