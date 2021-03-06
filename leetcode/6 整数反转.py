class Solution:
    def reverse(self, x: int) -> int:


        res = 0
        x2 = abs(x)

        while True:
            # 注意先求anum,再对x2的值进行更新
            anum = x2 % 10
            x2 = x2 // 10

            res = res * 10 + anum

            if x2 == 0:
                break

        # 边界条件
        if x >= 0 and res <= pow(2,31) - 1:
            return res
        if x < 0 and -res >= -pow(2,31):
            return -res
        return 0

        # x = 123
        # x2 = 123
        # (1) x2 = 12
        #     anum = 3
        #     res = 0 * 10 + 3
        # (2) x2 != 0
        #     x2 = 1
        #     anum = 2
        #     res = 3 * 10 + 2
        # (3) ...