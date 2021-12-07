dict1 = {1: 'one', 2: 'two', 3: 'three'}
print(dict1[1])
dict2 = {}
dict2 = dict((('F', 70), ('i', 105), ('s', 115), ('h', 104)))
print(dict2)
dict3 = dict(小甲鱼='让编程改变世界', HHH='努力才是王道')
print(dict3)
dict3['小甲鱼'] = '教你编程'
print(dict3)
dict3['爱迪生'] = "天才在此"
print(dict3)

# fromkeys
dict4 = {}
print(dict4.fromkeys((1, 2, 3)))
print(dict4.fromkeys((1, 2, 3), 'number'))
print(dict4.fromkeys((1, 2, 3), ('one', 'two', 'three')))

for i in dict1.keys():      # 键
    print(i)
for i in dict1.values():
    print(i)
print(dict1.get(1))
print(dict1.get(4, '没有'))

# 浅拷贝
# 地址改变，另开个数值，改变另开的数值不改变原来的
dict5 = {1: 'one', 2: 'two', 3: 'three'}
dict6 = dict5.copy()
dict7 = dict5
print(dict5, id(dict5))
print(dict6, id(dict6))  # 浅拷贝
print(dict7, id(dict7))
dict5[4] = 'four'
print(dict5)
print(dict6)
print(dict7)

print(dict5.pop(2))     # 消去
print(dict5)

print(dict5.setdefault(5, 'five'))
print(dict5)
