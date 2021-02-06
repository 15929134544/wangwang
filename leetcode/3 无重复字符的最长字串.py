class Solution:
    def lengthOfLongestSubstring(self, s):
        if len(s) == 0:
            return 0
        temp = set()
        ans =  0
        # i是左指针，right是右指针
        right, i = -1,0
        n = len(s)
        for i in range(n):
            if i != 0:  # i ！= 0 说明有和s[0]重复的字符
                temp.remove(s[i-1])
            while right+1 < n and s[right+1] not in temp:
                temp.add(s[right+1])
                right += 1
            ans = max(ans, right-i+1)
        return ans