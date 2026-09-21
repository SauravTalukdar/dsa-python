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
        i = m -1 #last real element in nums1 (index m-1)
        j = n -1 #last element in nums2 (index n-1)
        k = m+n -1 #last position in nums1 (index m+n-1) — where we place next element
        #For nums1=[1,2,3,0,0,0], m=3, nums2=[2,5,6], n=3:
        # i=2 → nums1[2]=3
        # j=2 → nums2[2]=6
        # k=5 → nums1[5]=0 (placeholder)
        while i >= 0 and j >=0: #run till both lists are exhausted(we are backward traversing so we check >=0)
            if nums1[i] > nums2[j]: #if nums1[i] > #nums2[j]
                nums1[k] = nums1[i] #place the element num1[i] in k position of nums1
                i-=1 #move i left
            else:
                nums1[k] = nums2[j] #else place nums2[j] in k position of nums1
                j-=1 #move j left
            k-=1 #keep moving k left after each placement, so that next element goes to one place left
        while j >=0: #remaining elements in nums2
            nums1[k] = nums2[j] #place them in the nums1[k] directly
            j-=1
            k-=1    
        # Why no tail loop for i?
        # If i still has elements — they're already in nums1 in the correct positions. No need to move them.    

        

