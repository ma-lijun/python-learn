# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-

# n! = {1, if n=0; n*(n-1)!, if n>0}

def fact(n):
    n = int(n)
    if n == 0:
        return 1
    else:
        return n * fact(n-1)


def print_num_recursive(n):
    if n > 0:
        print_num_recursive(n-1)
        print(n)


def print_num_recursive_revserve(n):
    if n > 0:
        print(n)
        print_num_recursive_revserve(n-1)  # 尾递归：递归在末尾调用


def hanoi_move(n, source, dest, intermediate):
    """
    问题是仍要想办法如何移动上边的 4 个盘子，我们可以同样的方式来移动上边的 4 个盘子，这就是一种递归的解法。 给定 n 个盘子和三个杆分别是 源杆(Source), 目标杆(Destination)，和中介杆(Intermediate)，我们可以定义如下递归操作：
        把上边的 n-1 个盘子从 S 移动到 I，借助 D 杆
        把最底下的盘子从 S 移动到 D
        把 n-1 个盘子从 I 移动到 D，借助 S
    """
    if n >= 1:  # 递归出口，只剩一个盘子
        hanoi_move(n-1, source, intermediate, dest)
        print("Move %s -> %s" % (source, dest))
        hanoi_move(n-1, intermediate, dest, source)


if __name__ == '__main__':
    # print(fact(10.1))
    # print_num_recursive(10)
    # print_num_recursive_revserve(10)

    hanoi_move(3, 'A', 'C', 'B')

