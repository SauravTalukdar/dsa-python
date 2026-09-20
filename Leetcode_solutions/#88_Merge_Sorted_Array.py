# Problem: Merge Sorted Array
# LeetCode: #88
# Difficulty: Easy
# Time Complexity: O(m+n)
# Space Complexity: O(1) — in place modification
# Approach: Start from end — compare from back, fill from back
# Key insight: filling right to left avoids overwriting unprocessed elements
# nums1 has m+n size with zeros as placeholders for nums2 elements

#we are given two sorted arrays in non decreasing order(increasing order),
#and two integers m and n representing number of elements in nums1 and nums2 respectively
#we need to merge both the arrays in increasing order
#we dont need to return the new sorted array,we need to store it in the nums1 array

#restrictions - we need to merge m part of nums1(it consists of m+n) and nums2(which is n)

#test cases
test0 = {
    'input' : {
        'nums1': [1,2,3,0,0,0],'m' : 3,
        'nums2' : [2,5,6],'n' : 3
    }, 'output' : [1,2,2,3,5,6]
}
test1 = {
    'input' : {
        'nums1': [1],'m' : 1,
        'nums2' : [],'n' : 0
    }, 'output' : [1]
}
test2 = {
    'input' : {
        'nums1': [0],'m' : 0,
        'nums2' : [1],'n' : 1
    }, 'output' : [1]
}
test3 = {
    'input' : {
        'nums1': [0],'m' : 0,
        'nums2' : [],'n' : 0
    }, 'output' : []
}
test4 = {
    'input' : {
        'nums1': [],'m' : 0,
        'nums2' : [],'n' : 0
    }, 'output' : []
}
test5 = {
    'input' : {
        'nums1': [1,2,9],'m' : 3,
        'nums2' : [5,6,8],'n' : 3
    }, 'output' : [1,2,5,6,8,9]
}

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i,j,k= m -1,n -1,m+n -1
        while i >= 0 and j >=0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i-=1
            else:
                nums1[k] = nums2[j]
                j-=1
            k-=1       
        while j >=0:
            nums1[k] = nums2[j]
            j-=1
            k-=1

        

