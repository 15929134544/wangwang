class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 重要

        # 存取前面读取的字符
        stack = []

        # 将对应关系存起来
        lookup = {'(': ')', '{': '}', '[': ']'}

        for parenthese in s:
            # 括号在lookup里面，压入stack里面
            if parenthese in lookup:
                stack.append(parenthese)
            # 如果不在，判断是否和栈顶匹配
            # 不匹配或者stack为空，但是此时只匹配到了一个右括号的情况
            elif len(stack) == 0 or lookup[stack.pop()] != parenthese:
                return False

        # 排除只有一个左括号的情况
        return len(stack) == 0





