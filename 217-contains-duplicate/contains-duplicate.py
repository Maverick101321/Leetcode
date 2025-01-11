class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #sorting way
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False