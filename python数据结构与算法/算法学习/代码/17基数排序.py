def radix_sort(li):
	max_num = max(li)  # 最大值 9->1, 99->2, 888->3, 10000->5
	it = 0  # it是用来判断排的是哪一位(十位个位)上的数
	while 10 ** it <= max_num:
		buckets = [[] for _ in range(10)]
		for var in li:
			digit = (var // 10 ** it) % 10
			buckets[digit].append(var)
		# 分桶完成
		print(buckets)
		li.clear()
		for buc in buckets:
			li.extend(buc)
		# 把数重新写回li
		it += 1

import random
li = list(range(100))
random.shuffle(li)  # 将列表顺序打乱
print(li)
radix_sort(li)
print(li)