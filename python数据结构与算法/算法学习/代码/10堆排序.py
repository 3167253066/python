# 向下调整的实现
def sift(li, low, high):
    """

    :param li: 列表
    :param low: 堆的根节点位置
    :param high: 堆的最后一个元素位置
    :return:
    """
    i = low  # i指开始指向根节点
    j = 2 * i + 1  # j开始是左孩子下标
    tmp = li[low]  # 把根顶存起来
    while j <= high:  # 只要j位置有数
        if j + 1 <= high and li[j+1] > li[j]:  # 如果右孩子有数且比左孩子大
            j = j + 1  # j指向右孩子
        if li[j] > tmp:
            li[i] = li[j]
            i = j
            j = 2 * i + 1
        else:  # tmp更大， 把tmp放到i的位置上
            li[i] = tmp  # 把tmp放到某一级领导的位置上
            break
    else:
        li[i] = tmp  # 把tmp放到叶子节点上


# 构造堆
def heap_sort(li):
    n = len(li)
    for i in range((n-2)//2, -1, -1):
        # i表示建堆的时候调整的部分的根的下标、
        sift(li, i, n-1)
    # 建堆完成了
    print(li)

    for i in range(n-1, -1, -1):
        # i指向当前堆的最后一个元素
        li[0], li[i] = li[i], li[0]  # 堆顶元素与最下面元素交换
        sift(li, 0, i - 1)  # i-1是新的high


li = [i for i in range(100)]
import random
random.shuffle(li)
print(li)

heap_sort(li)
print(li)
