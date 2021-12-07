try:
    sum = 1 + '1'
except OSError as reason:
    print("出错了，错误的原因是:" + str(reason))
except TypeError as reason:
    print("出错了，错误的原因是：" + str(reason))

try:
    sum = 1 + '1'
except (OSError,TypeError):
    print("出错了")
finally:
    print("我一定会执行")

raise ZeroDivisionError("除数为0的异常")
