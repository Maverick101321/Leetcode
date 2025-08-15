class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mid_index = len(nums) // 2
        hashmap = {}
        for i in nums:
            if i not in hashmap:
                hashmap[i] = 1
            else:
                hashmap[i] += 1
        for key, value in hashmap.items():
            if value > mid_index:
                return key
        return -1