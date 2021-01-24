"""
给你一根长度为n的绳子，请把绳子剪成整数长的m段（m、n都是整数，n>1并且m>1，m<=n），
每段绳子的长度记为k[1],...,k[m]。请问k[1]x...xk[m]可能的最大乘积是多少？
例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。
"""


# -*- coding:utf-8 -*-
class Solution:
    def cutRope(self, number):
        # write code here
        # 两种方法：
        """
        1.动态规划：f(n) = f(i) * f(n-i)
        2.贪心算法：当n>4的时候，3(n-3) >= 2(n-2)
        应当多剪3，让剩下的都是2这样的组合
        但是当剩余4的时候，不应该再剪3，应该剪成2和2

        """
        # 动态规划
        # if number == 2:
        #     return 2
        # if number == 3:
        #     return 3
        # if number == 4:
        #     return 4
        # maxList = [0, 1, 2, 3]
        # for i in range(4, number + 1):
        #     max = 0
        #     for j in range(1, i // 2 + 1):
        #         temp = maxList[j] * maxList[i - j]
        #         if temp > max:
        #             max = temp
        #     maxList.append(max)
        # return maxList[number]

        # 贪心算法：
        if number < 2 or number > 60:
            return False
        if number in (2, 3, 4):
            return  number
        timeoutThree = number // 3
        if number - timeoutThree * 3 == 1:
            timeoutThree -= 1
        timeoutTwo = (number - (timeoutThree * 3)) // 2
        max = pow(3, timeoutThree) ** pow(2, timeoutTwo)
        return max