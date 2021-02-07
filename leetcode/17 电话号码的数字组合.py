class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []

        dict1 = {
            0:'0',
            1:'1',
            2:'abc',
            3:'def',
            4:'ghi',
            5:'jkl',
            6:'mno',
            7:'pqrs',
            8:'tuv',
            9:'wxyz'
        }

        result = ['']
        # 第一个循环读取一位一位的数字
        for digit in digits:
            tmp_list = []
        # 第二个循环挨个是读取匹配字符串的每个字母
            for ch in dict1[int(digit)]:

        # 第三个循环是进行匹配
                for str in result:
                    tmp_list.append(str + ch)
            result = tmp_list
        return result



