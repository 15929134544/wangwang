class Solution:
    def longestPalindrome(self, s):
        size = len(s)

        if size < 2:  # 空串和一个字符都是回文
            return s

        max_length = 1
        start = 0  # 用来保存当前最长回文串的第一个字符下标

        # 创建二维数组，长度为size*size，将此二维数组上的所有格子的值设置为False
        dp = [[False for _ in range(size)] for _ in range(size)]

        # 对角线上的字符串都是回文串
        for i in range(size):
            dp[i][i] = True

        # 二重循环字符串，尾指针j从1开始到字符串结尾， 头指针i从0开始到j结束
        for j in range(1, size):
            for i in range(0, j):
                if s[i] == s[j]:  # 首尾字符相同
                    if j - i < 3:  # 并且字符串长度小于4，一定是回文串
                        dp[i][j] = True
                    else:
                        # 本级子串是否是回文串， 取决于下层本级子串的子串，如果
                        # 子串的子串是回文串，那么本机子串一定是回文串
                        # 这就是动态规划算法的关键：使用下层已经解决的问题来解决上层问题
                        dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = False

                if dp[i][j]:  # 如果是回文串，判断是否是最长回文串
                    cur_len = j - i + 1  # 当前回文串的长度
                    if cur_len > max_length:
                        max_length = cur_len
                        start = i

        return s[start: start + max_length]