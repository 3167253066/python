# 定义加法的行为：   __add__(self,other)
# 定义减法的行为：   __sub__(self,other)
# 定义乘法的行为：   __mul__(self,other)
# 定义真除法的行为：   __truediv__(self,other)
# 定义整数除法的行为：   __floordiv__(self,other)
# 定义取模算法的行为：   __mod__(self,other)
#...


class New_int(int):
    def __add__(self, other):
            return int.__sub__(self, other)

    def __sub__(self, other):
            return int.__add__(self,other)


a = New_int(3)
b = New_int(5)

print(a)
print(a + b)
print(b)
print(a - b)
        # 定义反运算
        # 定义增值运算