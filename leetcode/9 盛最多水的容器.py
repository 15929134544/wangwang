class Solution:
    def maxArea(self, height: List[int]) -> int:
        # result保存最大的面积
        left = 0
        right = len(height) - 1
        result = 0

        """
        使用双指针
        左边小于右边，那么就将左边的指针右移
        """
        while left < right:  # left要一直在right左边
            # 求面积
            water = min(height[left], height[right]) * (right - left)

            if water > result:
                result = water

            if height[left] < height[right]:
                left += 1
            else:  # 包含相等
                right -= 1
        return result