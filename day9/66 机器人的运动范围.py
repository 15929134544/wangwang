"""
地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，
每一次只能向左，右，上，下四个方向移动一格，但是不能进入行坐标
和列坐标的数位之和大于k的格子。
例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。
但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？



注：访问结点时，利用坐标访问在数组中的结点的下标
cury * cols + curx
"""


# -*- coding:utf-8 -*-
class Solution:
    def movingCount(self, threshold, rows, cols):
        # write code here
        # 和矩阵中的路径思路一致，但是对位置的约束条件不同，
        # 都是使用回溯法
        if rows < 1 or cols < 0 or threshold < 0:
            return 0
        visited = [0] * (rows * cols)
        return self.moving(threshold, rows, cols, 0, 0, visited)

    def moving(self, threshold, rows, cols, curx, cury, visited):
        cnt = 0
        if 0 <= curx < cols and 0 <= cury < rows and not visited[cols * cury + curx]:

            if self.calbitsum(curx) + self.calbitsum(cury) <= threshold:
                visited[cols * cury + curx] = True
                cnt = 1 + self.moving(threshold, rows, cols, curx, cury - 1, visited) \
                      + self.moving(threshold, rows, cols, curx, cury + 1, visited) \
                      + self.moving(threshold, rows, cols, curx - 1, cury, visited) \
                      + self.moving(threshold, rows, cols, curx + 1, cury, visited)
        return cnt

    def calbitsum(self, x):
        resum = 0
        while x != 0:
            resum += x % 10
            x /= 10
        return resum