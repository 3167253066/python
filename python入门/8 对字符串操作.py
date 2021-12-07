str1 = 'I love fishc.com'
print(str1[:6])
print(str1[2])
str2 = str1[:6] + '插入的字符串' + str1[6:]
print(str2)
str3 = 'xiaoxie'
print(str3.capitalize())        # 将字符串第一个字符大写
str4 = 'DAXIExiaoxie'
print(str4.casefold())          # 将字符串的所有字符变小写
print(str2.center(40))          #给定宽度，字符串居中
#用的较多的以下
str5 = 'Fishc'
print(str5.join('12345'))       #将str5插入到'12345'中
str6 = 'I love you'
print(str6.replace('you','she'))  #将you换成she
print(str6.split())             #分割后成为列表
print(str6.split("o"))