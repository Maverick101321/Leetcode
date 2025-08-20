class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currmax = nums[0]
        currmin = nums[0]
        maxprod = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]
            temp = max(num, num * currmax, num * currmin)
            currmin = min(num, num * currmax, num * currmin)
            currmax = temp
            maxprod = max(maxprod, currmax)
        return maxprod