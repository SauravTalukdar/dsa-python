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

#brute force solution
def arrProduct(nums):
    answer = []
    for i in range(len(nums)):
        product = 1
        for j in range(len(nums)):
            if i != j:
                product *= nums[j]
        answer.append(product)
    return answer

tests = [test0,test1,test2,test3,test4,test5,test6,test7]

for i,t in enumerate(tests):
    result = arrProduct(**t['input'])
    print(i, "PASSED" if result == t['output'] else "FAILED")


