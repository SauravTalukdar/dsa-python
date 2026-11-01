#Ask questions to get the whole picture of the problem(ask for examples to a question if not given already)
#Writing comments for code becomes code easier to read for the interviewer
#We can explain brute force solution first verbally

#Question - You are given an array of number(non-negative). Find a continuos subarray of the list which adds upto a given sum.
# [1,7,4,2,1,3,11,5] here the sum is 10(example). So the continuos subarray will be 4,2,1,3.
#we return the first and last index(last index plus one) of the subarray

#input and output(example test case)
arr0 = [1,7,4,2,1,3]
target0 = 10
output = 2,6


def subarray_sum(arr,target):
    pass

#test cases
'''
1. Generic subarray where the subarray is at the center
2. Subarray could be at the start
3. Subarray could be at the end
4. There is no subarray that adds up to 10(ask the interviewer what then)
5. You have a few zeros in the list
6. There are multiple subarrays in the array with the same sum(ask the interviewer what then)
7. Empty array
8. The subarray is a single element
'''

#brute force solution

def subarray_sum1(arr,target):
    n = len(arr)
    #i goes from 0 to n
    for i in range(0,n):
        #j goes from i to n+1
        for j in range(i,n+1):
            #check if subarray sum equals target
            if sum(arr[i:j]) == target:
                #answer found
                return i,j
    return None,None #if no subarray(or empty)      

print(subarray_sum1(arr0,target0))           

