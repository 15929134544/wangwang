class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # # 思路一：

        # # 空字符串
        # if not strs:
        #     return ''

        # for index in range(len(strs[0])):
        #     # 把第一个字符串的每个字母依次和后面每个字符串的字母做比较
        #     for str in strs[1:]:
        #         # 两种情况：
        #         # 1.完全一样就接着判断下一个
        #         # 2.不一样就直接返回
        #        # index >= len(str)应该写在之前
        #         if index >= len(str) or str[index] != strs[0][index]:
        #             # 如果不同直接返回前面相同的值
        #             return strs[0][:index]
        # return strs[0]


        # 思路二
        result = ''
        index = 0
        while True:
            try:
                # 利用去重来判断每个字母是否相同
                sets = set(str[index] for str in strs)
                if len(sets) == 1:
                    result += sets.pop()
                    index += 1
                else:
                    break

            except Exception as e:
                break
        return result