a = list()
b = 'I love you'
b = list(b)
print(b)
c = (1, 1, 2, 3, 5, 8, 13, 21, 34)
c = list(c)     # 将元组转换成列表
print(c)
print(len(b))

print(max(1, 2, 3, 4, 5))  # 用max,min时数据类型必须相同
print(max(b))       # 用字母的...码进行比较
chars = '12345678'
print(min(chars))
tuple1 = (3.1, 3.2, 3.3)
print(sum(tuple1))  # 求和
list1 = [2.5, 4, 7, 4, 2, 1, 9, 78]
print(sorted(list1))        #从小到大排序
list2 = list(reversed(list1))
print(list2)
list3 = list(enumerate(list1))
print(list3)

a = [1,2,3,4,5,6,7]
b = [4,5,6,7,8]
print(zip(a,b))
tuple1 = list(zip(a,b))
print(tuple1)
