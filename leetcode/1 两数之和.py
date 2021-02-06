class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for index, num in enumerate(nums):
            if target - num in hashmap:
                return [hashmap[target-num], index]
            else:
                hashmap[num] = index