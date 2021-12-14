# 导入库， 画图
import pandas as pd
import matplotlib.pyplot as plt
# #读取csv文件
aodi = pd.DataFrame(pd.read_csv('aodi.csv'))
print(aodi)

# 检查重复值
print(aodi.duplicated())
# 删除重复值
aodi = aodi.drop_duplicates()


# 清洗文字左右空格
aodi['型号'] = aodi['型号'].map(str.strip)
aodi['车龄'] = aodi['车龄'].map(str.strip)
aodi['里程'] = aodi['里程'].map(str.strip)
print(aodi.head())


# 车龄占比饼图
plt.rcParams['font.sans-serif'] = ['SimHei']  #解决乱码问题
df_score = aodi['车龄'].value_counts()  # 统计评分情况
plt.title("车龄占比图")  # 设置饼图标题
plt.pie(df_score.values,labels = df_score.index,autopct='%1.1f%%')  # 绘图
# autopct表示圆里面的文本格式，在python里%操作符可用于格式化字符串操作
plt.show()


# 车龄与车辆个数 # 年份与车辆数的关系， 柱状图
dict1 = {}
for i in aodi['车龄']:
    if i in dict1:
        dict1[i] = dict1[i] + 1
    else:
        dict1[i] = 1

print(dict1)
plt.bar(list(dict1.keys()), list(dict1.values()), color="orange")  # 水平方向
plt.xticks(color='red')
plt.yticks(color='blue')
plt.xlabel("车龄")
plt.ylabel("车辆数")
plt.show()


# #绘制散点图查看关系
price = []
year = []
# 价格数据清洗 &#60146;.&#59246;&#59854;万
for i in aodi['价格']:
    # print(i)
    price.append(i.split(';')[0][2:])
for i in aodi['车龄']:
    year.append(i)
print(year)
print(price)
plt.xticks(color='red')
plt.yticks(color='blue')
plt.xlabel("车龄")
plt.ylabel("价格")
plt.scatter(year, price)
plt.show()