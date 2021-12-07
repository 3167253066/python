# 注意比较区别，细节
def MySecondFunction(name):
    print(name + 'I love you')


MySecondFunction('小甲鱼 ')


def add(num1, num2):
    result = num1 + num2
    print(result)


add(3,4)


def add2(num1,num2):
    result = num1 + num2
    return result               #带返回值
print(add2(2,3))


# 形参，实参

def MyFirstFunction(name):
    '函数定义过程中name为形参'
    print('传递进来的' + name +'为实参，因为他是具体的参数值')
MyFirstFunction("HHH")


def SaySome(name,words):
    print(name + '-->' + words)


SaySome('小甲鱼','让编程改变世界')        #注意参数顺序
SaySome(words ='让编程改变世界',name='小甲鱼')


def SaySome2(name='小甲鱼', words='让编程改变世界'):
    print(name + "-->" + words)


SaySome2()
SaySome2('HHH')
SaySome2('HHH',"666")


def text(*params):
    print('参数的长度是：', len(params))
    print("第二个参数为：", params[1])


text(1, '小甲鱼', 3.41, 5, 6, 7)


def text1(*params , exp):
    print('参数的长度是：', len(params), exp)


text1(1,'小甲鱼',3.41,5,6,7,exp = 8)


#全局变量与局部变量
def discounts(price, rate):
    global final_price
    final_price = price * rate      # 变成了全局变量
    old_price = 50                  # 同上
    print("1修改后的old_price为：",old_price)# 1#
    return final_price


old_price = float(input('请输入原价:'))
rate = float(input('输入折扣率:'))
new_price = discounts(old_price, rate)
print("2修改后的old_price为：", old_price)     #2
print(final_price)
print('打折后的价格是:',new_price)


# ！！！！！python支持函数嵌套

# 函数闭包
def FunX(x):
    def FunY(y):
        return x*y      # FunY()闭包函数
    return FunY
i = FunX(5)
print(i(3))
print(FunX(5)(3))

def Fun1():
    x = 5           #这个x Fun2()将其看为局部变量
    def Fun2():
        nonlocal x      #声明x不是局部变量
        x *= x
        return x
    return Fun2()
print(Fun1())


# lambda函数
def add2(x, y):
    return x + y


print(add2(3, 4))


g = lambda x, y: x + y
print(g(3, 4))

# 映射
print(list(map(lambda x: x*2, range(10))))
# map将,后的全当做变量，带入lambda


