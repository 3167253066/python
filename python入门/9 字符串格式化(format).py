print("{0} love {1}.{2}".format("I","Fishc","com"))
print("{a} love {b}.{c}".format(a = "I",b = "Fishc",c = "com"))
print('\ta')        #转义符
print('\\')
print("{{0}}".format("bu"))
print("{0:10.1f}{1}".format(27.658,"GB"))       #10为数据长度，1为小数点后位数。末尾四舍五入

print("%c" % 97)
print("%c%c %c" % (97,98,99))
print("%s" % 'I love you')
print("%d + %d = %d" % (4,5,4+5))
print("%o" % 10)        #八进制
print("%x" % 10)
print("%X" % 10)        #十六进制
print("%f" % 27.658)    #默认六位小数
print("%e" % 27.658)

print("%10.1f" % 27.658)#10为数据长度，1为小数点后位数。末尾四舍五入
print("%10d" % 5)