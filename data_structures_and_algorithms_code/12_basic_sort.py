# -*- coding: utf-8 -*-
import random

# todo 冒泡排序 比较n轮， 每次相邻两个两两比较，不是正序相邻交换
# 冒泡排序
def bubble_sort(seq):  # O(n^2), n(n-1)/2 = 1/2(n^2+n)
    n = len(seq)
    for i in range(n-1):
        print(seq)
        for j in range(n-1-i):
            if seq[j] > seq[j+1]:
                seq[j+1], seq[j] = seq[j], seq[j+1]
        print(seq)


def test_bubble_sort():
    seq = list(range(10))  # 注意 python3 返回迭代器，所以我都用 list 强转了，python2 range 返回的就是 list
    random.shuffle(seq)   # shuffle inplace 操作，打乱数组
    bubble_sort(seq)
    assert seq == sorted(seq)


if __name__ == '__main__':
    test_bubble_sort()
