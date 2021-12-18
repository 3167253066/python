# 每个节点有两个指针


class Node(object):
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prior = None


# 双链表节点的插入 p
# p.next() = curNode.next
# curNode.next.prior = p
# p.prior = curNode
# curNode.next = p


# 双链表节点的删除
# p = curNode.next
# curNode.next = p.next
# p.next.prior = curNode
# del p
