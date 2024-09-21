class Solution:
    def canJump(self, nums: List[int]) -> bool:
        v = 0
        for i in nums:
            if v < 0:
                return False
            elif i > v:
                v = i
            v -= 1
        return True