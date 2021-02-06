class Solution:
    def myAtoi(self, s: str) -> int:
        # 去掉空格
        str = s.strip()
        if len(str) == 0:
            return 0

        symbols = '-+'
        ds = '0123456789'

        res = 0

        dist = [achar for achar in ds]
        ddict = {ele: idx for idx, ele in enumerate(dist)}

        sign = 1
        if str[0] == '+':
            sign = 1
        elif str[0] == '-':
            sign = -1

        for j in range(0, len(str)):
            # if j==0:
            if str[j] in '-+':
                if j == 0:
                    continue
            if not str[j] in ddict:
                break
            res = res * 10 + ddict[str[j]]

        MAX = pow(2, 31) - 1
        MIN = -MAX - 1

        if sign == 1:
            return res if res <= MAX else MAX
        else:
            return -res if -res >= MIN else MIN