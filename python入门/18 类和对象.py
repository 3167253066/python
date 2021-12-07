        # ## 面对对象编程
# 对象 = 属性 + 方法


class Turtle:       # python类名
    # 属性
    color = 'green'
    weight = 10
    legs = 4
    shell = True

    # 方法
    def climb(self, name):  # !!!!默认要求把self写进第一个，默认没有参数
        print("我正在努力的爬"+name)

    def run(self):
        prnit("我正在快跑")

    def bite(self):
        print("咬死你")
# 使用时

tt = Turtle()
tt.climb("math")
tt.bite()

# 面向对象 封装，继承，多态
# 例如列表的append  insert方法就是封装好的
# 继承就忘列表里加东西，从而永久改变其内容
# 魔法方法__init__(self)


class Person():
    __name = "小甲鱼"
    def getName(self):
        return self.__name

# 必须这样调用


p = Person()
print(p.getName())      #1
print(p._Person__name)  #2