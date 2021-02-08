class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # 空串或者haystack长度小于needle，返回0

        if not needle and len(haystack) < len(needle):
            return 0

        len1 = len(haystack)
        len2 = len(needle)

        for i in range(len1-len2+1):
            if haystack[i:i+len2] == needle:
                return i
        return -1