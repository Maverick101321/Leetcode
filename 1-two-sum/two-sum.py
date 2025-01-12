class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        prevsum = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevsum:
                return[prevsum[diff], i]
            prevsum[n] = i
            