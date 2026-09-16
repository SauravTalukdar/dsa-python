# Insertion Sort - Two Implementations

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

# Version 1: Manual shifting
# Time Complexity: O(n²)
# Space: O(1)
def insertion_sort(nums):
    for i in range(1,len(nums)): #we start from the 2nd index(1) till the last
        cur = nums[i] #we store the value of 2nd index in cur(current)
        j = i-1 #j is the index of one index before current
        while j>= 0  and nums[j] > cur: #while the left of current is greater than current(and while j is not less than 0th index)
            nums[j+1] = nums[j] #we shift j(the left of current)to one step right 
            j -= 1 #we make the value of j one step left of it to keep comparing if its greater than current
        nums[j+1] = cur # after the loop ends, we get the position to insert the element and we insert it in the gap
    return nums 

# Version 2: Python built-ins,pop and insert(we dont shift manually)
# Time Complexity: O(n²)
# Space: O(n),pop and insert create internal copies
def insertion_sort1(nums):
    for i in range(len(nums)):
        cur = nums.pop(i)# we pop the i element and store it in cur
        j = i - 1
        while j>=0 and nums[j] > cur:
            j -= 1
        nums.insert(j+1,cur) #we insert the cur in j+1 index
    return nums            

#testing
nums0, output0 = test0['input']['nums'], test0['output']
print('Input:', nums0)
print('Expected output:', output0)
result0 = insertion_sort(nums0)
print('Actual output:', result0)  



