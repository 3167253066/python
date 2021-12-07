# 递归求阶乘
def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)


number = int(input("请输入一个正整数："))
result = factorial(number)
print("%d的阶乘为：%d" % (number,result))


# 斐波那契数列
def fab(n):
    if n < 1:
        print("输入错误！")
        return -1
    elif n == 1 or n == 2:
        return 1
    else:
        return fab(n-1) + fab(n-2)

result = fab(20)

if result != -1:
    print("%d" % result)