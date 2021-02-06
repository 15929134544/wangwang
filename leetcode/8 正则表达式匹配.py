class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # 动态规划 填表
        # 分别在s和p前面分别加一个空字符
        # 当p出现*号时，比如ab*可以是和s的a匹配，可以将b看作零次重复
        # 所以要判断本格需要关注上一个和上上一个的情况

        # 当一个格子上面两个都为False，那么就需要判断*前的字母与s该下标字母是否匹配和
        # 左边一格的情况共同判断

        # 构建二维数组
        cache = [[False]*(len(s)+1) for _ in range(len(p)+1)]
        cache[0][0] = True
        for i in range(1, len(p)):
            # 对第一列进行初始化
            # 如果第二个字符时*，那么就要看前面的前面是否匹配
            cache[i+1][0] = cache[i-1][0] and p[i] == '*'
        # 从左到右，从上到下更新二维数组
        for i in range(len(p)):
            for j in range(len(s)):
                if p[i] == '*':
                    # *可以代表0个或者多个，此时要关注上一个和上上一个
                    # 如果上面两个都是False，那么要
                    cache[i+1][j+1] = cache[i][j+1] or cache[i-1][j+1]
                    if p[i-1] == s[j] or p[i-1] == '.':
                        cache[i+1][j+1] |= cache[i+1][j]
                # p不是*时，我们只需判断s与p的当前字母是否相同，而且左上角的元素是否为True
                else:
                    cache[i+1][j+1] = cache[i][j] and (p[i] == s[j] or p[i] == '.')
        return cache[-1][-1]