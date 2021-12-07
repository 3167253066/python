class Parent:
    def hello(self):
        print("正在调用父类方法。。。")


class Child(Parent):
    pass


p = Parent()
p.hello()
c = Child()
c.hello()
# 如果子类中定义与父类同名的方法或属性，则会自动覆盖父类的方法或属性


import random as r


class Fish:
    def __init__(self):
        self.x = r.randint(0, 10)
        self.y = r.randint(0, 10)

    def move(self):
        self.x -= 1
        print("我的位置是:", self.x, self.y)


class Goldfish(Fish):
    pass


class Carp(Fish):
    pass


class Salmon(Fish):
    pass


class Shark(Fish):
    def __init__(self):     # 这时候就覆盖了
        # 可以super().__init__()
        # 也可Fish.__init__()
        self.hungry = True

    def eat(self):
        if self.hungry:
            print("吃过了")
            self.hungry = False
        else:
            print("太撑了，")


fish = Fish()
fish.move()
fish.move()

shark = Shark()
shark.eat()

# 也有多重继承（难搞）




