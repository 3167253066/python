string = "Fishc"
it = iter(string)  # 转为可迭代
print(next(it))
# # print(next(it))
# # print(next(it))

while True:
    try:
        each = next(it)
    except StopIteration:
        break
    print(each)


# class Fibs:
#     def __init__(self):
#         self.a = 0
#         self.b = 1
#
#     def __iter__(self):  # 将这个类变成可迭代的
#         return self
#
#     def __next__(self):
#         self.a, self.b = self.b, self.a + self.b
#         return self.a
#
#
# for i in Fibs():
#     print(i)

# 注意强制关闭，否则后果不堪设想
