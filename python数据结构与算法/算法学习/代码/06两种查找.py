from cal_time import *
# import cal_time
# 时间复杂度O(n)
# 顺序查找

# 为了查出来这个数在列表中的位置
@cal_time
def liner_search(li, val):
    for ind, v in enumerate(li):  # enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标
        if v == val:
            return ind
        else:
            return None


# 二分查找
# 时间复杂度 O(logn)


@cal_time
def binary_search(li, val):  # li：表示列表， val：表示待查找的值
    left = 0
    right = len(li) - 1
    while left <= right:  # 说明候选区有值
        mid = (left + right) // 2
        if li[mid] == val:
            return mid
        elif li[mid] > val:  # 待查找的值在mid左侧
            right = mid - 1
        else:  # li[mid] < val 待查找的值在mid右侧
            left = mid + 1
    else:
        return None


li = [1, 2, 3, 4, 5, 6, 7, 8]
# li = list(range(100000))
# liner_search(li, 38900)
# binary_search(li, 38900)
print(binary_search(li, 3))


# 二分法更快，但是二分法需要提前进行排序，如果排序后只查找一次，用顺序查找就行
