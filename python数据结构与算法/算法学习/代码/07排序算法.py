import random

# 冒泡排序， 时间复杂度O(n*n)


# def bubble_sort(li):
#     for i in range(len(li)-1):  # 表示第i趟
#         for j in range(len(li)-i-1):
#             if li[j] > li[j+1]:
#                 li[j], li[j+1] = li[j+1], li[j]
#         print(li)
#
#
# li = [3, 2, 4, 6, 5, 9, 8, 7, 1]
# print(li)
#
# bubble_sort(li)


# 冒泡排序优化

def bubble_sort(li):
    for i in range(len(li)-1):  # 表示第i趟
        # print(i)
        exchange = False
        for j in range(len(li)-i-1):  # 已经排好的就不用比较了
            if li[j] > li[j+1]:
                li[j], li[j + 1] = li[j + 1], li[j]
                exchange = True
        # print(li)
        if not exchange:
            return
        else:
            print(li)


li = [9, 8, 7, 1, 2, 3, 4, 6, 5]
# print(li)
bubble_sort(li)
print("__________________________________________________________________________")

# 选择排序
# 简单选择排序

# def select_sort_simple(li):
#     li_new = []
#     for i in range(len(li)):
#         min_val = min(li)
#         li_new.append(min_val)
#         li.remove(min_val)
#     return li_new
#
# li = [3, 2, 4, 1, 5, 6, 8, 7, 9]
# print(select_sort_simple(li))

# 真正选择排序


# def select_sort(li):  # 先把最小的数选出来放到列表前面
#     for i in range(len(li) - 1):  # i是第几遍
#         min_loc = i
#         for j in range(i+1, len(li)):
#             if li[j] < li[min_loc]:
#                 min_loc = j
#         li[i], li[min_loc] = li[min_loc], li[i]
#         print(li)
#
#
# li = [3, 4, 2, 1, 5, 6, 8, 7, 9]
# print(li)
# select_sort(li)
