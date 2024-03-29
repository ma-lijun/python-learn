# -*- coding: utf-8 -*-


class Node(object):
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        """方便调试"""
        return '<Node: value :{}, next={}>'.format(self.value, self.next)

    __repr__ = __str__


class LinkedList(object):
    """ 链接表 ADT
     [root] -> [node0] -> [node1] -> [node2]
     """

    def __init__(self, maxsize=None):
        """
        : param maxsize: int or None , 如果是None 可以无限扩充
        """
        self.maxsize = maxsize
        self.root = Node() # 默认 root 节点指向 None
        self.tailnode = None
        self.length = 0

    def __len__(self):
        return self.length

    def append(self, value):  # 0(1)
        if self.maxsize is not None and len(self) >= self.maxsize:
            raise Exception("Linkedlist is Full")
        node = Node(value)  # 构造节点
        tailnode = self.tailnode
        if tailnode is None:  # 还没有 append 过， length = 0, 追加到root 后
            self.root.next = node
        else:
            tailnode.next = node
        self.tailnode = node
        self.length += 1

    def appendleft(self, value):
        if self.maxsize is not None and len(self) >= self.maxsize:
            raise Exception('LinkedList is Full')
        node = Node(value)
        if self.tailnode is None:
            self.tailnode = node

        headnode = self.root.next
        self.root.next = node
        node.next = headnode
        self.length += 1

    def __iter__(self):
        for node in self.iter_node():
            yield node.value

    def iter_node(self):
        """遍历 从 head 节点到 tail 节点"""
        curnode = self.root.next
        while curnode is not self.tailnode:
            yield curnode
            curnode = curnode.next
        if curnode is not None:
            yield curnode

    def remove(self, value):
        prenode = self.root
        for curnode in self.iter_node():
            if curnode.next == value:
                prenode.next = curnode.next
                if curnode is self.tailnode:  # 注意更新tailnode
                    if prenode is self.root:
                        self.tailnode = None
                    else:
                        self.tailnode = prenode
                del curnode
                self.length -= 1
                return 1  # 表明删除成功
            else:
                prenode =curnode
            return -1  # 表明删除失败

    def find(self, value):   # O(n)
        """
        查找一个节点， 返回序号， 从0 开始

        ：param value:
        """
        index = 0
        for node in self.iter_node():
            if node.value == value:
                return index
        index += 1
        return -1  # 没有找到

    def popleft(self):  # O(1)
        """
        删除第一个链表节点
        """
        if self.root.next is None:
            raise Exception("pop from empty LinkedList")
        headnode = self.root.next
        self.root.next = headnode.next
        self.length -= 1
        value = headnode.value

        if self.tailnode is headnode:  #
            self.tailnode = None
        del headnode
        return value

    def clear(self):
        for node in self.iter_node():
            del node
        self.root.next = None
        self.length = 0
        self.tailnode = None

    def reverse(self):
        """反转链表"""
        curnode = self.root.next
        self.tailnode = curnode
        prevnode = None

        while curnode:
            nextnode = curnode.next
            curnode.next = prevnode
            if nextnode is None:
                self.root.next = curnode

            prevnode = curnode
            curnode = nextnode


def test_linked_list():
    ll = LinkedList()

    ll.append(0)
    ll.append(1)
    ll.append(2)
    ll.append(3)

    assert len(ll) == 4
    # assert ll.find(2) == 2
    assert ll.find(-1) == -1

    # assert ll.remove(0) == 1
    assert ll.remove(10) == -1
    # assert ll.remove(2) == 1
    # assert len(ll) == 2
    # assert list(ll) == [1, 3]
    # assert ll.find(0) == -1

    ll.appendleft(0)
    # assert list(ll) == [0,1,3]
    # assert len(ll) == 3

    # headvalue == ll.popleft()
    # assert headvalue == 0
    # assert len(ll) == 2
    # assert list(ll) == [1, 3]

    # assert ll.popleft() == 1
    # assert list(ll) == [3]
    # ll.popleft()
    # assert len(ll) == 0
    # assert ll.tailnode is None
    #
    # ll.clear()
    # assert len(ll) == 0
    # assert list(ll) == []


def test_linked_list_remove():
    ll = LinkedList()
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    ll.append(7)
    ll.append(7)
    print(list(ll))

def test_single_node():
    ll = LinkedList()
    ll.append(0)
    ll.remove(0)
    ll.appendleft(1)
    assert list(ll) == [1, 0]


def test_linked_list_reverse():
    ll = LinkedList()
    n = 10
    for i in range(n):
        ll.append(i)
    ll.reverse()
    assert list(ll) == list(reversed(range(n)))


def test_linked_list_append():
    ll = LinkedList()
    ll.append(1)
    ll.appendleft(2)
    # assert list(ll) == [1, 2]


if __name__ == '__main__':
    test_single_node()
    test_linked_list()
    test_linked_list_append()
    test_linked_list_reverse()


if __name__ == '__main__':
    a = Node()
    # print(a, Node, Node())
