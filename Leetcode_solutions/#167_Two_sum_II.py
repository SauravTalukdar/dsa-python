# Problem: Two sum
# Leetcode: #167
# Difficulty: Medium
# Approach 1: Using nested loops.  O(n^2) time, O(1) space

'''
Given a list of numbers sorted in ascending order and a target number,
find the two numbers (at different positions) that add up to the target.
Return their positions as [first, second], counting positions from 1(1-indexed)(not 0).
There is always exactly one answer.
Only constant extra space is allowed (no dictionary or extra list).

Example: numbers = [2, 7, 11, 15], target = 9
         2 + 7 = 9, positions 1 and 2  →  [1, 2]
'''

#test cases
test0 = {
    'input' : {
        'nums': [2,7,11,15],
        'target': 9,
    },'output': [1,2]
}  

test1 = {
    'input' : {
        'nums': [2,3,4],
        'target': 6,
    },'output': [1,3]
}  

test2 = {
    'input' : {
        'nums': [-1,0],
        'target': -1,
    },'output': [1,2]
}  

test3 = {
    'input' : {
        'nums': [2,2,5],
        'target': 4,
    },'output': [1,2]
}  

test4 = {
    'input' : {
        'nums': [-3,-1,2,5],
        'target': 4,
    },'output': [2,4]
} 

tests = [test0,test1,test2,test3,test4]

#brute force
def two_sum_II(nums,target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                return [i+1,j+1]              

for i,t in enumerate(tests):
    result = two_sum_II(**t['input'])
    print(i, "PASSED" if result == t['output'] else "FAILED")

