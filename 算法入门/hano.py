def hanoi(n, a, b, c):
    if n > 0:
        # 1.把n-1个盘子从A经过C移动到B
        hanoi(n-1, a, c, b)
        # 2.把第n个盘子从A移动到C
        print("moving from %s to %s" % (a, c))
        # 3.把n-1个盘子从B经过A移动到C
        hanoi(n-1, b, a, c)


hanoi(3, 'A', 'B', 'C')
