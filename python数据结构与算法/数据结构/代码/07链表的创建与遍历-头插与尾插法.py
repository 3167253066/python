class Node:
    def __init__(self, item):
        self.item = item
        self.next = None


def create_linklist_head(li):
    head = Node(li[0])
    for element in li[1:]:
        node = Node(element)
        node.next = head
        head = node
    return head


def create_linklist_tail(li):
    head = Node(li[0])
    tail = head
    for element in li[1:]:
        node = Node(element)
        tail.next = node
        tail = node
    return head


def print_linklist(lk):
    while lk:
        print(lk.item, end=',')
        lk = lk.next


lk = create_linklist_head([1, 2, 3])
print_linklist(lk)


# 链表的插入
# p.next = curNode.next
# curNode.next = p


# 链表结点的删除
# p = curNode.next
# curNode.next = curNode.next.next
# del p
