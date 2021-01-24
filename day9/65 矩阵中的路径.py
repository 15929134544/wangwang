"""
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下
移动一个格子。如果一条路径经过了矩阵中的某一个格子，则该路径不能再进入该格子。
"""


# -*- coding:utf-8 -*-
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        # 使用回溯法：
        """
        首先在矩阵中找到字符串中的第一个字符，对其上下左右的
        字符进行判断，如果其中有和第二个字符相同的，那么就把
        这个字符作为起点，一直重复这个过程

        """
        if not matrix and rows <= 0 and cols <= 0 and path == None:
            return False
        boolmatrix = [0] * (cols * rows)
        pathLength = 0
        for row in range(rows):
            for col in range(cols):
                if self.hasPathCore(matrix, rows, cols, row, col, path, pathLength, boolmatrix):
                    return True
        return False

    def hasPathCore(self, matrix, rows, cols, row, col, path, pathLength, boolmatrix):
        if len(path) == pathLength:
            return True

        hasNextPath = False
        if (0 <= row < rows and 0 <= col < cols and matrix[row * cols + col] == path[pathLength] and not boolmatrix[
            row * cols + col]):
            pathLength += 1
            boolmatrix[row * cols + col] = True
            hasNextPath = (self.hasPathCore(matrix, rows, cols, row - 1, col, path, pathLength, boolmatrix) or
                           self.hasPathCore(matrix, rows, cols, row + 1, col, path, pathLength, boolmatrix) or
                           self.hasPathCore(matrix, rows, cols, row, col - 1, path, pathLength, boolmatrix) or
                           self.hasPathCore(matrix, rows, cols, row, col + 1, path, pathLength, boolmatrix))
            if not hasNextPath:  # 四个点都没有路径
                # 则回退到上一个点
                pathLength -= 1
                # 将该点设置为为标记点
                boolmatrix[row * cols + col] = False
        return hasNextPath