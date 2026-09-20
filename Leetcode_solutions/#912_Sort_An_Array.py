# Problem : Sort an array
# Leetcode : #912
# Difficulty : Medium
# Time Complexity: O(n log n) — always, no worst case degradation
# Space Complexity: O(n) — extra space for merging
# Approach: Divide and conquer
# Key insight: merging two sorted lists is O(n)

class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2 
        left = nums[:mid]   
        right = nums[mid:]
        left_sorted,right_sorted = self.sortArray(left),self.sortArray(right)
        sorted_nums = self.merge(left_sorted,right_sorted)
        return sorted_nums
    def merge(self,nums1,nums2):
        merged = []
        i,j = 0,0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                merged.append(nums1[i])
                i+=1
            else:
                merged.append(nums2[j])
                j+=1 
        nums1_tail = nums1[i:]                 
        nums2_tail = nums2[j:] 
        return merged + nums1_tail + nums2_tail                

        