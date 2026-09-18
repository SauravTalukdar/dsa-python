# Merge Sort
# Time Complexity: O(n log n) — always, no worst case degradation
# Space Complexity: O(n) — extra space for merging
# Approach: Divide and conquer
#   Divide: split into halves until single elements
#   Conquer: merge sorted halves back together
# Key insight: merging two sorted lists is O(n)

#we will use divide and conquer for implementing merge sort

#if our list contain 1 or less elements(0) it is already sorted, so we return it(base case)
#if not,we divide the unsorted list into two almost equal halves
#sort each halve recursively with merge sort algorithm. we will get back two sorted list
#merge the two sorted lists to get a single sorted list

#test cases

#list with random numbers
test0 = {
    'input' : {
        'nums' : [4,2,6,3,4,6,2,1]
    },
    'output' : [1,2,2,3,4,4,6,6]
}
#another list with random numbers
test1 = {
    'input' : {
        'nums' : [5,2,6,1,23,7,-12,12,-243,0]
    },
    'output' : [-243,-12,0,1,2,5,6,7,12,23]
}
#list thats already sorted
test2 = {
    'input' : {
        'nums' : [3,5,6,8,9,10,99]
    },
    'output' : [3,5,6,8,9,10,99]
}
#list thats sorted in decreasing order
test3 = {
    'input' : {
        'nums' : [99,10,9,8,6,5,3]
    },
    'output' : [3,5,6,8,9,10,99]
}
#list containing repeating elements
test4 = {
    'input' : {
        'nums' : [5,-12,2,6,1,23,7,7,-12,6,12,1,-243,1,0]
    },
    'output' : [-243,-12,-12,0,1,1,1,2,5,6,6,7,7,12,23]
}
#empty list
test5 = {
    'input' : {
        'nums' : []
    },
    'output' : []
}
#list with one element
test6 = {
    'input' : {
        'nums' : [23]
    },
    'output' : [23]
}
#list with one element repeating multiple times
test7 = {
    'input' : {
        'nums' : [42,42,42,42,42,42,42,42]
    },
    'output' : [42,42,42,42,42,42,42,42]
}

def merge_sort(nums):
    if len(nums) <= 1: #terminating comdition(list of 0 or 1 elements)
        return nums
    #get the midpoint
    mid = len(nums) // 2 
    #split into two halves
    left = nums[:mid]  #left half of the list  
    right = nums[mid:] #right half of the list

    left_sorted,right_sorted = merge_sort(left),merge_sort(right) #recurcively sort left and right halves

    sorted_nums = merge(left_sorted,right_sorted)

    return sorted_nums

def merge(nums1,nums2): #we take two sorted arrays
    merged = [] #will store the list here
    i,j = 0,0 #staring i and j index from zero
    while i < len(nums1) and j < len(nums2): #runs till one of the list gets exhausted
        if nums1[i] <=nums2[j]: #if left is less than right
            merged.append(nums1[i]) #append the value in the list
            i +=1 #increase the first lists i
        else:
            merged.append(nums2[j]) # else right is less than left append the value in the list
            j +=1 #increase the second list j
    #one list will end(will be empty) and the other remaining list will contain remaining elements 
    nums1_tail = nums1[i:] #store the rest of first list(may be empty)
    nums2_tail = nums2[j:] #store the rest of second list(may be empty)

    return merged + nums1_tail + nums2_tail #add all and return 

#testing cases

nums0, output0 = test0['input']['nums'], test0['output']
print('Input:', nums0)
print('Expected output:', output0)
result0 = merge_sort(nums0)
print('Actual output:', result0)  

nums3, output3 = test3['input']['nums'], test3['output']
print('Input:', nums3)
print('Expected output:', output3)
result3 = merge_sort(nums3)
print('Actual output:', result3) 

nums5, output5 = test5['input']['nums'], test5['output']
print('Input:', nums5)
print('Expected output:', output5)
result5 = merge_sort(nums5)
print('Actual output:', result5)  




    



