# Quick Sort
# Time Complexity: O(n log n) average, O(n²) worst case (sorted input with last element as pivot)
# Space Complexity: O(1) — sorts in place, no extra lists
# Key difference from merge sort: sorts in place, no extra space needed

#Quick sort is useful when we dont want additional space for the input

#In quick sort we check if an array contains 1 or less elements, then we return it as its already sorted(base case)
#Else we pick a pivot point from the array,it can be any random element
#If we pick an element say index 2 we move that to the end of the list and go from there
#Or we can pick the last element as the pivot(convinient)
#After that we put two pointers, one at the start and one at last just before pivot
#Then we do comparisons,the elements lesser than the pivot go to its left and the elements greater than the pivot go to its right
#The pivot element divides the array into two halves which can be sorted independently by making recursive calls to quicksort

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

def quick_sort(nums,start = 0,end = None):
    if end is None:
        # nums = list(nums) might not add this
        end = len(nums) - 1 #end is the last index
    if start < end: #till we reach the last
        pivot = partition(nums,start,end) #store the pivot point
        quick_sort(nums,start,pivot-1) #recursively sort left of pivot
        quick_sort(nums,pivot+1,end) #recurcively sort right of pivot
    return nums #return the sorted array

def partition(nums,start = 0,end = None):
    if end is None:
        end = len(nums) -1
    l,r = start,end - 1 #left(l) index is start(0) and right(r) is one less than end(end is the pivot)
    while r >l: #Keep going while pointers haven't crossed
        if nums[l] <= nums[end]:#Left element is smaller than or equal to pivot,it's already on the correct side.
            l +=1 #Move l right.
        elif nums[r] > nums[end]: #Right element is larger than pivot — it's already on the correct side.
            r -=1 # Move r left.
        else:
            nums[l],nums[r] = nums[r],nums[l] #Left element is larger than pivot AND right element is smaller
            #than pivot — both are on wrong sides. Swap them. Both move to correct sides.
    if nums[l] > nums[end]: #Loop ended,l is where pivot belongs.
        nums[l],nums[end] = nums[end],nums[l]#If element at l is greater than pivot,swap pivot into position l.
        return l
    else:
        return end #otherwise pivot stays at end.Return pivot's final position.                  
        
#testing cases

nums0, output0 = test0['input']['nums'], test0['output']
print('Input:', nums0)
print('Expected output:', output0)
result0 = quick_sort(nums0)
print('Actual output:', result0)  

nums3, output3 = test3['input']['nums'], test3['output']
print('Input:', nums3)
print('Expected output:', output3)
result3 = quick_sort(nums3)
print('Actual output:', result3) 

nums5, output5 = test5['input']['nums'], test5['output']
print('Input:', nums5)
print('Expected output:', output5)
result5 = quick_sort(nums5)
print('Actual output:', result5) 