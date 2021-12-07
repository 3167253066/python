
# 创建普通列表
list1 = ['小甲鱼', '小布丁', '黑夜', '迷途', '恬静']
list2 = ['1', '2', '3', '4', '5']
# 创建混合列表
list3 = [1, '小甲鱼', 3.14, [1, 2, 3]]
len(list1)  # 可查看长度
# 向列表增加元素
list1.append('葫芦娃')  # 向列表添加元素到末尾
print(list1)

list1.extend(['竹林小溪', '迷恋'])
print(list1)             # 添加多个

list1.insert(0, '牡丹')    # 可选添加位置0开始
print(list1)

# 删除元素
list1.remove("牡丹")
print(list1)

del list1[0]    # del list1可删除整个列表
print(list1)

list1.pop(0)
print(list1.pop(0))
print(list1)

# 切片
print(list2)
print(list2[:3])
print(list2[3:])
print(list2[:])

# 列表中用逻辑符
list11 = [123]
list12 = [234]
print(list11 > list12)
list11 = [123, 456]
list12 = [234, 123]
print(list11 > list12)  # 比较列表中第一个元素
list13 = [123, 456]
print((list11 < list12) and (list11 == list13))

list14 = list11 + list12
print(list14)

list13 = list13 * 3
print(list13)

list13 *= 3
print(list13)

print(123 in list13)
print('小甲鱼' not in list13)
list15 = [123, ['小甲鱼', '牡丹'], 456]
print('小甲鱼' in list15)
print('小甲鱼' in list15[1])
print(list15[1][1])
print(list13)
print(list13.count(123))   # 统计123在列表中出现的次数
print(list13.index(123))    # 统计123在列表中第一次出现的位置
print(list13.index(123, 3, 7))  # 从3位置开始，统计123在列表中第一次出现的位置
list13.reverse()  # 反转
print(list13)
list16 = [4, 2, 5, 1, 9, 13]
list16.sort()  # 排序
print(list16)
list16.sort(reverse=True)  # T必须大写
print(list16)