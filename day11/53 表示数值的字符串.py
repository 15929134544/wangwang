"""
请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。
但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是。
"""


class Solution:
    def isNumeric(self, s):
        hasE = False
        hasDot = False
        hasSign = False
        for i in range(len(s)):
            if s[i] == 'e' or s[i] == 'E':
                ''' 判断有没有e '''
                if hasE or i == len(s) - 1:
                    return False
                hasE = True
            elif s[i] == '.':
                if hasDot or hasE:
                    return False
                hasDot = True
            elif s[i] == '+' or s[i] == '-':
                if hasSign and s[i-1] != 'e' and s[i-1] != 'E':
                    return False
                if not hasSign:
                    if i != 0 and s[i-1] != 'e' and s[i-1] != 'E':
                        return False
                hasSign = True
            else:
                if s[i] < '0' or s[i] > '9':
                    return False
        return True

