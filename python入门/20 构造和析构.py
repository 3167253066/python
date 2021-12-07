class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getPeri(self):
        return (self.x + self.y) * 2

    def getArea(self):
        return self.x * self.y


rect = Rectangle(3,4)  # 形参直接就传给了Rectangle的 __init__
print(rect.getPeri())
print(rect.getArea())


# 2
class CapStr(str):
    def __new__(cls, string):
        string = string.upper()
        # return string
        return str.__new__(cls, string)


a = CapStr("I love hhh")
print(a)