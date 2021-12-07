#集合不支持用下标索引     set
num1 = {1,2,3,4,5,6,4,3,2,1} #不允许重复
print(num1)
set1 = set([1,2,3,4,5,6,4,3,2,1])
print(set1)

#去重
#1
num2 = [1,2,3,4,5,6,4,3,2,1]
temp = []
for i in num2:
    if i not in temp:
        temp.append(i)
print(temp)
#2
num3 = list(set(num2))
print(num3)

print(1 in num3)

num1.add(7)
print(num1)
num1.remove(7)
print(num1)

num4 = frozenset([1,2,3,4,5])  #不能再添加，或删除元素
print(num4)