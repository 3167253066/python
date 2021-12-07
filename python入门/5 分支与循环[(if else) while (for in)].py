# assert关键字"断言":当其后条件为假，程序自动崩溃，抛出AssertionError错误
# 分支
score = eval(input("请输入一个分数:"))
if 100 >= score >= 90:
    print("A")
elif 90 > score >= 80:
    print("B")
elif 80 > score >= 70:
    print("C")
elif 70 > score >= 60:
    print("D")
else:
    print("输入错误！")


# 高级
x, y = 4, 5
if x < y:
    small = x
else:
    small = y
# 可改为small = x if x < y else y


# while循环
i = 1
while i < 5:
    print(i)
    i = i+1


# for遍历
favorite = "Fishc"
for i in favorite:
    print(i, end=' ')   # end=''与end=' '，均可避免换行
print("\n")
member = ['小甲鱼', '小布丁', '黑皮', '迷途', '意境']
for each in member:
    print(each, len(each), len(member))  # 分别为列表长度和字符串长度


# range配合for
for i in range(5):
    print(i, end=' ')
print("\n")
for i in range(2,5):
    print(i, end=' ')
print("\n")
for i in range(1, 10, 2):    #三个参数，最后的为步长
    print(i, end=' ')
print("\n")


# break与continue
for i in range(10):
    if i % 2 != 0:
        print(i)
        continue    # 跳过本次循环
    i += 2
    print(i)

print(")))))))))))))))))))))))))))))))))))))))))))))))))))))")


for i in range(10):
    if i % 2 != 0:
        print(i)
        break       # 跳过全部循环
    i += 2
    print(i)
