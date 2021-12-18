def bucket_sort(li, n = 100, max_num = 10000):
	buckets = [[] for _ in range(n)]  # 创建空桶(空列表)
	print(buckets)
	for var in li:
		i = min(var // (max_num // n), n-1)  # i表示var放到几号桶里, 这里也为了当max_num=10000时的特殊情况
		buckets[i].append(var)  # 把var加到桶里面
		# 保持桶内有序
		for j in range(len(buckets[i])-1, 0, -1):  # 遍历每个桶
			if buckets[i][j] < buckets[i][j-1]:
				buckets[i][j], buckets[i][j-1] = buckets[i][j-1], buckets[i][j]
			else:
				break
	sorted_li = []
	for buc in buckets:
		sorted_li.extend(buc)  # 将列表合并
	return sorted_li


import random
li = [random.randint(0, 100) for i in range(1000)]
# print(li)
li = bucket_sort(li)
print(li)