def hanoi(n, a, b, c):  # 代表要将n个盘子，从a经过b移动到c
    if n > 0:
        hanoi(n-1, a, c, b)
        print("moving from %s to %s" % (a, c))
        hanoi(n-1, b, a, c)


hanoi(3, 'A', 'B', 'C')