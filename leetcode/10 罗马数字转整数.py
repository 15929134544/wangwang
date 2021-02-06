class Solution:
    def romanToInt(self, s: str) -> int:
        # 如果左边的字母小于右边，那就是相减
        dict1 = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        num = 0
        n = len(s)

        for index in range(n-1):
            if dict1[s[index]] < dict1[s[index+1]]:
                num -= dict1[s[index]]
            else:
                num += dict1[s[index]]
        return num+dict1[s[-1]]