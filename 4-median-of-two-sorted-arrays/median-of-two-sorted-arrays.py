class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        merged = nums1 + nums2
        
        merged.sort()

        total_len = len(merged)

        if total_len % 2 == 1:
            return merged[total_len // 2]
        else:
            first_element = merged[total_len // 2 - 1]
            second_element = merged[total_len // 2]
            return (first_element + second_element) / 2
        