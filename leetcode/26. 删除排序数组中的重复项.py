class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        if not nums:
           return 0

        count = 0   # 计算有多少个不同的数字
        for i in range(len(nums)):
            if nums[count] != nums[i]:
                count += 1
                # 要及时更新nums[count]
                nums[count] = nums[i]
        return count +1