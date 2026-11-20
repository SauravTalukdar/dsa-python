# Problem: Product of Array Except Self
# LeetCode: #238
# Difficulty: Medium
# Approach 1: brute force, for each i multiply every other element. O(n^2) time, O(1) extra space
# Approach 2: left and right products, no division. Time: O(n) | Space: O(n)
# Idea: answer[i] = (product of everything left of i) * (product of everything right of i)
#       left[i+1] = left[i] * nums[i]
#       right[j]  = right[j+1] * nums[j+1]
# Approach 3: in place with running prefix/postfix. Time: O(n) | Space: O(1) extra
# Idea: result holds left products after pass 1; pass 2 multiplies in the right products

'''
Given an integer array nums, 
return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
that means, for example - nums = [1,2,3,4], answer = [24,12,8,6].
here 24 is a product of everything other than 1(of nums), 12 is a product of everything other than 2, 8 is a product of everything 
other than 3 and 6 is the product of everything other than 4.
'''

#test cases
test0 = {
    'input' : {
        'nums': [1,2,3,4]
    },'output': [24,12,8,6]
}

test1 = {
    'input' : {
        'nums': [-1,1,0,-3,3]
    },'output': [0,0,9,0,0]
}

test2 = {
    'input' : {
        'nums': []
    },'output': []
}

test3 = {
    'input' : {
        'nums': [0,0,0,0]
    },'output': [0,0,0,0]
}

test4 = {
    'input' : {
        'nums': [1,0,1,0]
    },'output': [0,0,0,0]
}

test5 = {
    'input' : {
        'nums': [1, 2]
    },'output' : [2,1]
}

test6 = {
    'input' : {
        'nums': [1,0,3]
    },'output' : [0,3,0]
}

test7 = {
    'input' : {
        'nums': [-2,3,-1]
    },'output' : [-3,2,-6]
}

tests = [test0,test1,test2,test3,test4,test5,test6,test7]

#brute force solution
def arrProduct(nums):
    result = [] #store the product list
    for i in range(len(nums)):
        product = 1 
        for j in range(len(nums)):
            if i != j: #as our product will be everything minus the element(so when i not equal to j)
                product *= nums[j] # multiply every other element into product
        result.append(product) #append each product to the result
    return result

def arrProduct1(nums):
    left = [1] #initialize left with 1 as we need a 1 to the left of the first number
    right = [1] * len(nums) # everything else are placeholders; only the last slot (nothing to its right) contains a 1
    for i in range(len(nums)-1): #stops one short: the last element never contributes to a left product
        left.append(left[i]*nums[i]) #left[i] = product of everything before i; times nums[i] = product of everything before i+1 
    for j in range(len(nums)-2,-1,-1): #from the second-to-last index down to 0 (the last is already 1)
        right[j] = nums[j+1]*right[j+1] #right[j] = product of everything after j = next element * product after that
    return [left[i] * right[i] for i in range(len(nums))] #multiply both those lists(left and right) and return the answer 

def arrProduct2(nums):
    # same idea as left/right, but the two lists become two running numbers (extra space O(n) -> O(1))

    result = [1] * len(nums) #One slot per position, filled with placeholders. This is the output list, and it’s the only list we create.

    prefix = 1 #The running product of everything to the left of the current position. It starts at 1 because nothing is to the left of index 0.
    for i in range(len(nums)): #pass 1:left products
        result[i] = prefix #store the product of everything before i
        prefix *= nums[i] #now include nums[i], ready for the next position.

    postfix = 1 #the running product of everything to the right of the current position. It starts at 1 because nothing is to the right of the last index.
    for i in range(len(nums)-1,-1,-1): #the loop goes backwards to from last index to index 0
        result[i] *= postfix #multiply the left product already stored by the right product. That gives left × right.
        postfix *= nums[i] #include nums[i] for the next position to the left.
    return result   

'''
Trace on [1,2,3,4]

Pass 1 (prefix starts at 1):

i	result[i] = prefix	prefix after
0	    1	    1·1     = 1
1	    1	    1·2     = 2
2	    2	    2·3     = 6
3	    6	    6·4     = 24

result = [1, 1, 2, 6], which matches your left list.

Pass 2 (postfix starts at 1):

i	result[i] *= postfix	postfix after
3	   6·1     = 6	          1·4  = 4
2	   2·4     = 8	          4·3  = 12
1	   1·12    = 12	          12·2 = 24
0	   1·24    = 24	          24·1 = 24

result = [24, 12, 8, 6]
'''         

for i,t in enumerate(tests):
    result = arrProduct2(**t['input'])
    print(i, "PASSED" if result == t['output'] else "FAILED")


