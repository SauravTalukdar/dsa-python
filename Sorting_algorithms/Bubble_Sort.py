#sorting a list in ascending order

# Bubble Sort
# Time Complexity: O(n²)
# Space Complexity: O(1)
# Approach: Compare adjacent elements, swap if out of order
#           Largest element bubbles to end after each pass

#test cases(we will create dictionary with input and output)

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

def bubble_sort(nums):
    #if we create the copy its space complexity will be 0(n)
    nums = list(nums) #creating a copy of the list(so that we dont mix up or change our test cases,its not absolutely needed)
    for element in range(len(nums)-1): #run this process for n-1 times(so that we can keep pushing the greater number to the back)
        for i in range(len(nums)-1): #iterate over the array, except the last element(we dont compare the last elemen any further)
            if nums[i] > nums[i+1]: #if current number is greater than the next
                nums[i],nums[i+1] = nums[i+1],nums[i] #swap the numbers
    return nums #return the sorted array       

#testing for test case0
nums0,output0 = test0['input']['nums'],test0['output']
print('input:',nums0) 
print('expected output:',output0)
result0 = bubble_sort(nums0)
print('actual output:',result0) 

#we can test all the cases similarly

