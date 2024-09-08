class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        u = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[u] = nums[i]
                u += 1
        return u