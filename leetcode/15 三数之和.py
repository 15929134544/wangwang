class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 重要
        n = len(nums)
        result = []  # 保存最终的结果
        # 是将数组分为大于0小于0两部分的作用
        nums.sort()

        for i in range(n - 2):  # 需要3个数字
            # 两个判断条件
            if nums[i] + nums[i + 1] + nums[i + 2] > 0:
                break
            if nums[i] + nums[n - 2] + nums[n - 1] < 0:
                continue  # 往右移动一位
            if 0 < i and nums[i] == nums[i - 1]:
                continue  # 不希望找到重复的值
            # 从两头往中间找的方法
            left, right = i + 1, n - 1
            while left < right:
                temp = nums[i] + nums[left] + nums[right]
                if temp == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    while left + 1 < right and nums[left] == nums[left + 1]:
                        left += 1
                    left += 1
                    while left < right - 1 and nums[right] == nums[right - 1]:
                        right -= 1
                    right -= 1
                elif temp < 0:
                    left += 1
                else:
                    right -= 1
        return result








