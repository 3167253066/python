f = open("文件读取.txt", 'rt', encoding='utf-8')
print(f.read())
print(1, f.read(), 2)
f.close()

g = open("文件读取.txt", 'rt', encoding='utf-8')
print(g.read(5))
print(g.tell())  # 当前指针的位置
g.seek(45, 0)    # 修改指针位置
print(g.readline())
print(list(g))
g.seek(0, 0)
lines = list(g)
for i in lines:
    print(i)
g.close()

# 文件写入
with open("文件写入.txt", 'w', encoding='utf-8') as h:
    h.write('HHHHH')
    h.close()