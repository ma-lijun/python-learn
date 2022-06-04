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


# O(n^2) 对列表下标两层for 循环， 记录当前下标，寻找最小元素下班，判断下标是否相同，不同交换元素
def select_sort(seq):
    n = len(seq)
    for i in range(n-1):
        min_idx = i  # 假设当前下标的元素是最小的
        for j in range(i+1, n):  # 从i的后边开始找到最小的元素， 得到它的下标
            if seq[j] < seq[min_idx]:
                min_idx = j   # 一个 j 循环下来之后找到最小元素的小标
        if min_idx != i:  # swap
            seq[i], seq[min_idx] = seq[min_idx], seq[i]



def test_select_sort():
    seq = list(range(10))
    random.shuffle(seq)
    sorted_seq = sorted(seq)
    select_sort(seq)
    assert seq == sorted_seq


# 可以安装 玩扑克 来理解
def insertion_sort(seq):
    """
    每次挑选下一个元素插入已经排序的数组中，初始时已经排序数字钟只有一个元素
    """
    n = len(seq)
    print(seq)
    for i in range(1, n):
        value = seq[i]  # 保存当前位置的值， 转移过程可能会被覆盖
        pos = i
        while pos > 0 and value < seq[pos-1]:
            seq[pos] = seq[pos-1]
            pos -= 1
        seq[pos] = value  # 找到合适位置赋值就好




if __name__ == '__main__':
    test_bubble_sort()
