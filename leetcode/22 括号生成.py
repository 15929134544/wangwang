class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]

        """
        # 递归

        if n == 0:
            return []

        result = []

        self.helper(n, n, '', result)
        return result

    # left和right表示左括号剩余数量和右括号剩余数量
    # item保存中间结果
    # result保存最终结果
    def helper(self, left, right, item, result):
        # 如果右边剩余可以插入的数量大于左边剩余可以插入的数量
        if right < left:
            return
        if left == 0 and right == 0:
            result.append(item)
        if left > 0:
            self.helper(left-1, right, item + '(', result)
        if right > 0:
            self.helper(left, right-1, item + ')', result)


