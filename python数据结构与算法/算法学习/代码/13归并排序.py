# 时间复杂度 O(nlogn)
# 空间复杂度 O(n)


# 归并排序中归并的实现
def merge(li, low, mid, high):  # low为列表第一个数下标， high为最后一个数下标，mid为中间数下标
	i = low
	j = mid + 1
	ltmp = []
	while i <= mid and j <= high:  # 只要左右两边都有数
		if li[i] < li[j]:
			ltmp.append(li[i])
			i += 1
		else:
			ltmp.append(li[j])
			j += 1

	# while执行完肯定两边有一边没有数了
	while i <= mid:
		ltmp.append(li[i])
		i += 1
	while j <= high:
		ltmp.append(li[j])
		j += 1
	li[low : high+1] = ltmp  # 再把数写回去


# li = [2, 4, 5, 7, 1, 3, 6, 8]
# merge(li, 0, 3, 7)
# print(li)


# 归并排序实现
def merge_sort(li, low, high):
	if low < high:  # 至少有两个元素，递归
		mid = (low + high) // 2
		merge_sort(li, low, mid)
		merge_sort(li, mid+1, high)
		merge(li, low, mid, high)


li = list(range(1000))
import random
random.shuffle(li)
print(li)
merge_sort(li, 0, len(li)-1)
print(li)
print(li)
print(li)




# 便于理解
# def merge_sort_test(li, low, high):
# 	if low < high:  # 至少有两个元素，递归
# 		mid = (low + high) // 2
# 		merge_sort(li, low, mid)
# 		merge_sort(li, mid+1, high)
# 		print(li[low : high + 1])

# li = list(range(16))
# import random
# random.shuffle(li)
# print(li)
# merge_sort_test(li, 0, len(li)-1)
# print(li)
