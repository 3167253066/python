# 元组内容不可变
tuple1 = (1, 2, 3, 4, 5, 6, 7, 8)
print(tuple1[1])
print(tuple1[5:])   # 切片

tuple2 = tuple1[:]
print(tuple2)

tuple3 = (3,)
print(tuple3)  # 判定是不是元组要看,（逗号）
print(8*(8,))

tuple4 = ('小甲鱼', '黑夜', '迷途', '小布丁')
tuple4 = tuple4[:2] + ('恬静',) + tuple4[2:]   # 这样可向里面添加元素
print(tuple4)
# del tuple4   # 可删除整个元组