# 顺序查找 （O(n)）
# def sunxu(li, val):  # li: 为查找的列表， val: 要查找的值
#     a = 0
#     for x, y in enumerate(li):
#         if y == val:
#             a = 1
#             return x
#     if a == 0:
#         return None
#
#
# li = [1, 2, 3, 4, 5, 6, 7]
# result = sunxu(li, 8)
# print(result)


# 二分查找（折半查找） O(logn) 列表必须已经有序（从小到大排列）
# def zheban(li, val):
#     left = 0
#     right = len(li) - 1
#     while left <= right:
#         mid = (right + left) // 2  # 一定是加号
#         if li[mid] == val:
#             return mid
#         elif li[mid] > val:
#             right = mid - 1
#         elif li[mid] < val:
#             left = mid + 1
#     else:
#         return None
#
#
# li = [1, 2, 3, 4, 5, 6, 7, 8]
# result = zheban(li, 7)
# print(result)


# 冒泡排序(排成从小到大)
# def maopao(li):
#     for i in range(len(li)-1):  # 一次循环至少排列好一个，循环的次数
#         for j in range(len(li)-i-1):  # 已经排好的就不用比较了
#             if li[j] > li[j+1]:
#                 li[j], li[j+1] = li[j+1], li[j]
#         # print(li)  # 冒泡的过程，便于观察结果
#     return li
#
#
# li = [3, 5, 6, 8, 9, 0, 2, 7]
# result = maopao(li)
# print(result)


# 选择排序（结果从小到大）    每次循环是为了找到后面没排好的数里面的最小的，然后放在第i位置上
# def xuanze(li):
#     for i in range(len(li)-1):  # 循环的次数
#         min_val = i
#         for j in range(i+1, len(li)):  # 只循环没有排好的
#             if li[j] < li[min_val]:
#                 min_val = j
#             li[i], li[min_val] = li[min_val], li[i]
#         print(li)  # 选择的过程，便于观察结果
#     return li
#
#
# li = [2, 4, 6, 1, 7, 9, 3, 8, 0]
# result = xuanze(li)
# print(result)


# 插入排序  (不再开辟新的列表),所以要把已经排好的所有比要插的数大的数依次往后挪一位，把要插的数插进去
def charu(li):
    for i in range(1, len(li)):
        tmp = li[i]
        j = i - 1  # j 指的是手里牌的下标
        while j >= 0 and li[j] > tmp:
            li[j+1] = li[j]
            j -= 1
        li[j+1] = tmp
        print(li)  # 输出过程
    return li


li = [3, 2, 4, 1, 5, 7, 9, 6, 8]
result = charu(li)
print(result)


# 快速排序 (先从最左边找出一个数a， 再从列表最右边数开始跟a比较，发现比a小的数b，则把b放在a的位置上
# ，再从左取一个数c,跟a比较，如果比a大，则放在最初b的位置上，直到left下标 == right下标，把a放在空的位置上，
# 再递归a的左右两边即可)
# def hh(li, left, right):
#     tmp = li[left]
#     while left < right:
#         while left < right and li[right] >= tmp:  # 中间还有数，并且右边的数大于选的数a
#             right -= 1  # 继续向右边走
#         li[left] = li[right]  # 直到找出一个小于tmp的，将其放到选的数a的位置上
#         while left < right and li[left] <= tmp:
#             left += 1
#         li[right] = li[left]
#     li[left] = tmp  # 把tmp放到空位上
#     # li[right] = tmp  # 把tmp放到空位上,均可以
#     return left
#
#
# def kuaisu(li, left, right):
#     if left < right:
#         mid = hh(li, left, right)
#         print(li)
#         kuaisu(li, left, mid-1)
#         kuaisu(li, mid+1, right)
#
#
# li = [3, 4, 1, 6, 2, 7, 9, 8, 5]
# result = kuaisu(li, 0, len(li)-1)
# print(li)


# 堆排序（1. 建堆（通过先让最后一个非叶子节点进行调整，在找倒数第二个非叶子节点进行调整，直到根节点，则建好了堆））
# （2. 堆顶为最大的元素， 去掉堆顶，将最后一个元素放到堆顶，向下调整，又可以找到最大的，依次进行）
# （3. 向下调整，从根节点一步一步向下调整,(此时根节点的左右孩子都是调整好的)）
# 向下调整
# def xxtz(li, low, high):
#
#     """
#     :param li: 列表
#     :param low: 堆的根节点的位置
#     :param high: 堆的最后一个元素的位置
#     :return:
#     """
#     i = low  # i开始指向根节点
#     j = 2 * i + 1  # j 为根节点的左孩子
#     tmp = li[low]  # 存根顶元素
#     while j <= high:
#         if j + 1 <= high and li[j+1] > li[j]:  # 右孩子节点有数且比左孩子数大
#             j = j + 1
#         if li[j] > tmp:  # 孩子的数大约根节点的数时
#             li[i] = li[j]  # 根节点调整为其孩子
#             i = j  # 再依次开始调整孩子
#             j = j * 2 + 1
#         else:  # tmp比他的左右孩子都大
#             li[i] = tmp
#             break
#     else:  # 没有孩子了
#         li[i] = tmp
#
#
# # 建堆(如孩子下标为i, 父亲下标为(i-1)//2)
# def jd(li):
#     n = len(li)
#     for i in range((n-2)//2, -1, -1):  # n-1为孩子的下标
#         # i表示为建堆需要调整的非叶子节点的下标。从下往上
#         xxtz(li, i, n - 1)
#         # 建堆完成
#
#     for i in range(n-1, -1, -1):  # i指向堆的最后一个元素
#         li[0], li[i] = li[i], li[0]  # 堆顶元素与最下面元素交换,不开辟列外的列表空间
#         xxtz(li, 0, i-1)  # 堆的再后一个元素
#
#
# li = [2, 5, 7, 3, 1, 8, 0, 9, 4, 6]
# jd(li)
# print(li)


# 归并排序： 归并排序中归并的实现(前提是左右两边都是有序的)
# def gb(li, low, mid, high):  # low: 为列表第一个数下标， high:为最后一个
#     new_list = []
#     i = low
#     j = mid + 1
#     while i <= mid and j <= high:
#         if li[i] < li[j]:
#             new_list.append(li[i])
#             i += 1
#         else:
#             new_list.append(li[j])
#             j += 1
#     # while执行完两边有一边没有数了
#     while i <= mid:
#         new_list.append(li[i])
#         i += 1
#     while j <= high:
#         new_list.append(li[j])
#         j += 1
#     li[low: high + 1] = new_list  # 再把数写回去
#
#
# def gb_sort(li, low, high):
#     if low < high:  # 至少有两个元素，再递归
#         mid = (low + high) // 2
#         gb_sort(li, low, mid)
#         gb_sort(li, mid+1, high)
#         gb(li, low, mid, high)
#
#
# li = [2, 5, 7, 8, 4, 1, 6, 9, 0, 3]
# gb_sort(li, 0, len(li)-1)
# print(li)


# 希尔排序
# 希尔排序的时间复杂度比较复杂，并且和选取的gap序列有关
# （先分d组， 每组进行插入排序， 再分d/2组，每组插入排序，直到剩一组）
# def insert_sort_gap(li, gap):
#     for i in range(gap, len(li)):  # i 表示摸到的牌的下标
#         tmp = li[i]
#         j = i - gap  # j指的是手里牌的下标
#         while j >= 0 and li[j] > tmp:
#             li[j+gap] = li[j]
#             j -= gap
#             li[j+gap] = tmp
#
#
# def shell_sort(li):
#     d = len(li) // 2
#     while d >= 1:
#         insert_sort_gap(li, d)
#         d //= 2
#
#
# li = [2, 4, 7, 9, 3, 5, 8, 0, 1, 6]
# shell_sort(li)
# print(li)


# 计数排序（通过建立小列表，统计li每个元素出现的次数再排序）
# def jishu(li, max_count=100):
#     count = [0 for _ in range(max_count+1)]
#     for val in li:
#         count[val] += 1
#     li.clear()  # 不用建新的列表了
#     for j, val in enumerate(count):
#         for i in range(val):
#             li.append(j)
#
#
# import random
# li = [random.randint(0, 100) for _ in range(1000)]
# jishu(li)
# print(li)


# 桶排序（分成几个桶，每个桶里有数的范围，数对应放进去，并保持桶内有序）
# def t(li, n=100, max_count=10000):
#     kt = [[] for _ in range(n)]  # 创建空桶
#     for val in li:
#         i = min(val//(max_count//n), n - 1)  # 放到第几个桶内，这里也为了当max_num=10000时的特殊情况
#         kt[i].append(val)
#         # 保持桶内有序
#         for j in range(len(kt[i]) - 1, 0, -1):  # 遍历整个i号桶
#             if kt[i][j] < kt[i][j - 1]:
#                 kt[i][j], kt[i][j - 1] = kt[i][j - 1], kt[i][j]
#             else:
#                 break
#     sorted_li = []
#     for buc in kt:
#         sorted_li.extend(buc)  # 每个桶合并
#     return sorted_li
#
#
# import random
# li = [random.randint(0, 100) for i in range(1000)]
# print(li)
# li = t(li)
# print(li)


# 基数排序
# def js(li):
#     max_num = max(li)  # 最大值 9->1, 99->2, 888->3, 10000->5
#     it = 0  # it是用来判断排的是哪一位(十位个位)上的数
#     while 10 ** it <= max_num:
#         t = [[] for _ in range(10)]
#         for var in li:
#             digit = (var // 10 ** it) % 10
#             t[digit].append(var)
#             # 分桶完成
#         # print(t)
#         li.clear()
#         for buc in t:
#             li.extend(buc)
#         # 把数重新写回li
#         it += 1
#
#
# import random
# li = list(range(100))
# random.shuffle(li)
# print(li)
# js(li)
# print(li)


