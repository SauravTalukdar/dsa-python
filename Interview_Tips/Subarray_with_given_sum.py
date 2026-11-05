#Ask questions to get the whole picture of the problem(ask for examples to a question if not given already)
#Writing comments for code becomes code easier to read for the interviewer
#We can explain brute force solution first verbally
#Code the optimized solution or even convey what you want to do if you cant code it completely
#After that ask them if this is okay. If they say can you do better - there might be a more optimized solution

#Question - You are given an array of number(non-negative). Find a continuos subarray of the list which adds upto a given sum.
# [1,7,4,2,1,3,11,5] here the sum is 10(example). So the continuos subarray will be 4,2,1,3.
#we return the first and last index(last index plus one) of the subarray

# Problem: Subarray with given sum (non-negative numbers)
# Time: O(n) optimal | Space: O(1)
# Approach 1: brute force O(n^3) -> Approach 2: running sum O(n^2) -> Approach 3: sliding window O(n)
# Pattern: Sliding Window (non-negative only)

#input and output(example test case)
arr0 = [1,7,4,2,1,3,11,5]
target0 = 10
output0 = 2,6

arr1 = [4,2,1,3,11,5,1,7]
target1 = 10
output1 = 0,4

arr2 = [11,5,1,7,4,2,1,3]
target2 = 10
output2 = 4,8

arr3 = [11,5,1,7,4,2,1,3]
target3 = 25
output3 = None,None

#function signature
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

#1-brute force solution
#Time complexity - O(n^3),n for i loop then n for j loop then n for the sum inside if block

def subarray_sum1(arr,target):
    n = len(arr)
    #i goes from 0 to n-1
    for i in range(0,n): #i goes from 0 to one less than the last element
        #j goes from i to n
        for j in range(i,n+1): #j goes from i(which is 0 at first) to n
            #check if subarray sum equals target
            if sum(arr[i:j]) == target: #if we find the target in this range(eg- arr[2,6] = 4,2,1,3(then sum)==10)
                #answer found
                return i,j
    return None,None #if no subarray(or empty)      
   
#2-Running Sum(Optimized solution)
#maintain a running sum for the inner loop
#when the running sum exceeds the target,break out of inner that loop
#Time complextiy - O(n^2)

def subarray_sum2(arr,target):
    n = len(arr)
    #i goes from 0 to n-1
    for i in range(0,n):
        s = 0 #running sum
        #j goes from i to n
        for j in range(i,n+1):
            if s == target: #if our running sum is equal to target
                return i,j 
            elif s > target: #if its greater than target we break it(as if we keep increasing j the value will only become greater,adding more number cant decrease the sum)
                break
            if j < n: #this is a guard so that our j doesnt go further than n(end element)
                s += arr[j] #keep adding the next elements(arr[j]) to the running sum till we find if its equal to target
    return None,None              

#3-Sliding Window(Most optimized solution)
#Time complexity - O(n)

def subarray_sum3(arr,target):
    n = len(arr)
    i,j,s = 0,0,0 #we take i(left pointer), j(right pointer) and running sum s at 0
    while i < n and j < n+1: #run i till n and j till end + 1
        print(f"i:{i},j:{j},s:{s}") # to check each loops result
        if s == target: #if found return
            return i,j
        elif s < target: #if running sum is less grow the window
            if j < n: #guard
                s += arr[j] #by adding j to the window
            j += 1 #increase j(move the right pointer ahead)
        elif s > target: #if running sum is more the sum is to big, we shrink the window
            s -= arr[i] # we remove the leftmost number(i)
            i += 1 #then increase the i(move the left pointer forward)
    return None,None

print(subarray_sum3(arr0,target0))           
# print(subarray_sum3(arr1,target1))           
# print(subarray_sum3(arr2,target2))   
# print(subarray_sum3(arr3,target3))  

