# 导入库， 画图
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from PIL import Image

# #读取csv文件
aodi = pd.DataFrame(pd.read_excel('./car_33.xlsx', index_col=0))  # 去掉第一列的索引
# print(aodi.head())


# 数据清洗

# 检查是否有重复值， false为没重复
# print(aodi.duplicated())
# 删除重复值
aodi = aodi.drop_duplicates()


# 清洗文字左右空格
aodi['城市'] = aodi['城市'].map(str.strip)
aodi['车型'] = aodi['车型'].map(str.strip)
aodi['现价'] = aodi['现价'].map(str.strip)
aodi['首付'] = aodi['首付'].map(str.strip)
aodi['降价'] = aodi['降价'].map(str.strip)
aodi['里程'] = aodi['里程'].map(str.strip)
aodi['年份'] = aodi['年份'].map(str.strip)
aodi['过户'] = aodi['过户'].map(str.strip)

# print(aodi.head())


def nian(x):
    if len(x.split(':')) == 3:
        return x[:4] + '年'
    else:
        return x[:-3]

# 清洗 改正    2015-12-01T01:00:00Z  这种数据  为2015年
# 并且去掉年份中的月
aodi['年份'] = aodi['年份'].map(nian)
# print(aodi['年份'])


# 过户数据处理，将为'0过户'的改为0， 其他不处理
def hu(x):
    if x == "0过户":
        return 0
    else:
        return x
aodi['过户'] = aodi['过户'].map(hu)

# print(aodi['过户'])






# 车辆年份占比饼图
plt.rcParams['font.sans-serif'] = ['SimHei']  # 解决乱码问题
df_score = aodi['年份'].value_counts()
plt.title("车年份占比图")  # 设置饼图标题
plt.pie(df_score.values, labels=df_score.index, autopct='%1.1f%%')  # 绘图
# autopct表示圆里面的文本格式，在python里%操作符可用于格式化字符串操作
plt.show()




# 地区占比饼图（不加就删了）
plt.rcParams['font.sans-serif'] = ['SimHei']  # 解决乱码问题
df_score = aodi['城市'].value_counts()
plt.title("车城市占比图")  # 设置饼图标题
plt.pie(df_score.values, labels=df_score.index, autopct='%1.1f%%')  # 绘图
# autopct表示圆里面的文本格式，在python里%操作符可用于格式化字符串操作
plt.show()








# 地区与车辆数的关系， 柱状图
dict1 = {}
for i in aodi['城市']:
    if i in dict1:
        dict1[i] = dict1[i] + 1
    else:
        dict1[i] = 1
# print(dict1)
plt.bar(list(dict1.keys()), list(dict1.values()), color="orange")  # 水平方向
plt.xticks(color='red', rotation=60)  #倾斜60度
plt.yticks(color='skyblue')
plt.xlabel("地区")
plt.ylabel("车辆数")
plt.show()






# 统计车辆型号，词云展示个数最多的50个
# 字典类型统计各个车型的个数
type_car = aodi['车型'].values
dict_car_type = {}
for i in type_car:
    car = i.split(' ')[0].split('-')[0]
    if car in dict_car_type:
        dict_car_type[car] = dict_car_type[car] + 1
    else:
        dict_car_type[car] = 1
# print(dict_car_type)

# 找出品牌数最多的前50个
n = 50
L = sorted(dict_car_type.items(), key=lambda item: item[1], reverse=True)
L = L[:n]
dictdata = {}
for l in L:
    dictdata[l[0]] = l[1]
# print(dictdata.keys())
# print(dictdata.values())

# 准备词云要用的字， 例如：大众 123    123是大众出现的次数
str1 = ''
for i in range(len(dictdata.keys())):
    str1 = str1 + list(dictdata.keys())[i] + str(list(dictdata.values())[i]) + ' '
# print(str1)

alice_mask = np.array(Image.open("./02.png"))

# 词云配置，中文字题
my_wordcloud = WordCloud(background_color="white",font_path="./simhei.ttf", mask=alice_mask).generate(str1)
plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()






# 大众，里程数和价格的变化
index_ls = []
price = []
distance = []


for i in range(len(aodi['车型'].values)):
    if aodi['车型'].values[i].split(' ')[0].split('-')[0] == '大众':
        index_ls.append(i)
# aodi1 = []
for j in index_ls:
    # print(aodi[j:j+1]['现价'].values[0])
    price.append(float(aodi[j:j+1]['现价'].values[0][:-1]))
    distance.append(float(aodi[j:j+1]['里程'].values[0][:-3]))
print(price)
print(distance)

# # #品牌相同，绘制散点图查看价格与里程数的关系
plt.xticks(color='red')
plt.yticks(color='blue')
plt.xlabel("里程")
plt.ylabel("价格")
plt.scatter(distance, price)
plt.show()





# 大众，地区和价格的变化
index_ls = []
price = []
distance = []

# 选出车型为大众的
for i in range(len(aodi['车型'].values)):
    if aodi['车型'].values[i].split(' ')[0].split('-')[0] == '大众':
        index_ls.append(i)

# 处理车型为大众的现价与城市数据
for j in index_ls:
    price.append(float(aodi[j:j+1]['现价'].values[0][:-1]))
    distance.append(aodi[j:j+1]['城市'].values[0])
# print(price)
# # print(distance)

# # #品牌相同，绘制散点图查看地区与里程数的关系
plt.xticks(color='red')
plt.yticks(color='blue')
plt.xlabel("城市")
plt.ylabel("价格")
plt.scatter(distance, price)
plt.show()

