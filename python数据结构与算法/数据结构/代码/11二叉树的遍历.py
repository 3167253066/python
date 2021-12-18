from collections import deque


class BiTreeNode:
    def __init__(self, data):
        self.data = data
        self.lchild = None  # 左孩子
        self.rchild = None  # 右孩子


a = BiTreeNode("A")
b = BiTreeNode("B")
c = BiTreeNode("C")
d = BiTreeNode("D")
e = BiTreeNode("E")
f = BiTreeNode("F")
g = BiTreeNode("G")

e.lchild = a
e.rchild = g
a.rchild = c
c.lchild = b
c.rchild = d
g.rchild = f

root = e
print(root.lchild.rchild.data)


# 前序遍历   中左右
def pre_order(root):
    if root:
        print(root.data, end=",")
        pre_order(root.lchild)
        pre_order(root.rchild)


pre_order(root)
print()


# 中序遍历  左中右
def in_order(root):
    if root:
        in_order(root.lchild)
        print(root.data, end=",")
        in_order(root.rchild)


in_order(root)
print()


# 后序遍历   左右中
def post_order(root):
    if root:
        post_order(root.lchild)
        post_order(root.rchild)
        print(root.data, end=",")


post_order(root)
print()


# 层次遍历
def level_order(root):
    queue = deque()
    queue.append(root)
    while len(queue) > 0:  # 只要队不空
        node = queue.popleft()
        print(node.data, end=",")
        if node.lchild:
            queue.append(node.lchild)
        if node.rchild:
            queue.append(node.rchild)


level_order(root)


"""
         E
    A         G
       C          F
    B     D
"""