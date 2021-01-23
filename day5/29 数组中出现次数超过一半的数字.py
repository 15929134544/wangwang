"""
数组中有一个数字出现的次数超过数组长度的一半，
请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。
"""


class Solution:
    """第二种，假设有这个数字，那么它的数量一定比其它所有数字之和还要多，按照这个思路得出num，然后验证
    """
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if not numbers:
            return 0
        num = numbers[0]
        count = 1
        for i in range(1, len(numbers)):
            if numbers[i] == num:
                count += 1
            else:
                count -= 1
            if count == 0:
                num = numbers[i]
                count = 1
        count = 0
        for i in numbers:
            if i == num:
                count += 1
        return num if count > len(numbers) / 2.0 else 0


s = Solution()
num = [1,2,3,2,2,2,5,4,2]
res = s.MoreThanHalfNum_Solution(num)
print(res)